import json
from ..utils.utils import db
from flask import Flask




class Region(db.Model):
    __tablename__ = 'regions'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(45), nullable=False, unique=True)
    state = db.relationship('State', backref='regions', lazy=True)


    def __repr__(self):
        return f"<Region {self.name}>"

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)
    
    __table_args__ = (
        db.Index('idx_regions_name', 'name'),
    )
    


    
    
class State(db.Model):
    __tablename__ = 'states'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(45), nullable=False, unique=True)
    region = db.Column(db.String(45), nullable=False)
    region_id = db.Column(db.Integer(), db.ForeignKey('regions.id'), nullable=False)
    capital = db.Column(db.String(45))
    population = db.Column(db.String(100))
    area = db.Column(db.String(100))
    postal_code = db.Column(db.String(100))
    No_of_LGAs = db.Column(db.String(100))
    lgas = db.relationship('Lga', backref='state', lazy=True)

    



    def __repr__(self):
        return f"<State {self.name}>"

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)
    

    # Define an index on the 'name' column
    __table_args__ = (
        db.Index('idx_states_name', 'name'),
    )






class Lga(db.Model):
    __tablename__ = 'lga'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(45), nullable=False, unique=True)
    region_id = db.Column(db.Integer(), db.ForeignKey('regions.id'), nullable=False)
    state_id = db.Column(db.Integer(), db.ForeignKey('states.id'), nullable=False)

    def __repr__(self):
        return f"<City {self.name}>"

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)
    

class Area(db.Model):
    __tablename__ = 'areas'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(45), nullable=False, unique=True)
    state_id = db.Column(db.Integer(), db.ForeignKey('states.id'), nullable=False)
    city_id = db.Column(db.Integer(), db.ForeignKey('cities.id'), nullable=False)

    def __repr__(self):
        return f"<Area {self.name}>"

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)
    

    
class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(45), nullable=False, unique=True)
    region_id = db.Column(db.Integer(), db.ForeignKey('regions.id'), nullable=False)
    areas = db.relationship('Area', backref='city', lazy=True)

    def __repr__(self):
        return f"<City {self.name}>"

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)
    



def load_dataset():
    with open('api/models/dataset.json') as file:
        dataset = json.load(file)

    for region_data in dataset['Regions']:
        region = Region(
            name=region_data['name'],
        )
        
        db.session.add(region)

    for state_data in dataset['States']:
        state = State(
            name=state_data['name'],
            region=state_data['region'],
            region_id=state_data['region_id'],
            capital=state_data['capital'],
            population=state_data['population'],
            area=state_data['area'],
            postal_code=state_data['postal_code'],
            # No_of_LGAs=state_data['No_of_LGAs'],
            # lgas=state_data['lgas']
            )
        


        db.session.add(state)

    for lga_data in dataset['Lgas']:
        lga = Lga(
            name=lga_data['name'],
            code = lga_data['code'],
            headquarters = lga_data['headquarters'],
            zone = lga_data['zone'],
            senatorial_district = lga_data['senatorial_district'],
            area = lga_data['area'],
            population = lga_data['population'],
            description = lga_data['description'],
            image = lga_data['image'],
            state_id=lga_data['state_id'],
            region_id=lga_data['region_id']
            
            )
        db.session.add(lga)

        # Load other data models based on your dataset structure and relationships

    db.session.commit()
