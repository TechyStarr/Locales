import json
from ..utils.utils import db
from flask import Flask




class Region(db.Model):
    __tablename__ = 'regions'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(45), nullable=False)
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
    name = db.Column(db.String(45), nullable=False)
    region = db.Column(db.String(45), nullable=False)
    region_id = db.Column(db.Integer(), db.ForeignKey('regions.id'), nullable=False)
    capital = db.Column(db.String(45))
    population = db.Column(db.String(100))
    area = db.Column(db.String(100))
    postal_code = db.Column(db.String(100))
    # No_of_LGAs = db.Column(db.String(100))
    lgas = db.relationship('Lga', backref='state', lazy=True) # One to many relationship with Lga lazy=True means that the data is loaded on access

    



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
    __tablename__ = 'lgas'
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
            name=state_data['state'],
            region=state_data['region'],
            region_id=state_data['region_id'],
            capital=state_data['capital'],
            population=state_data['population'],
            # area=state_data['area'],
            # postal_code=state_data['postal_code'],
            # No_of_LGAs=state_data['No_of_LGAs'],
            )
        
    # for lga_name in dataset['lgas']: 
    #     lga = Lga(name=lga_name, state=state)

        db.session.add(state)

    
    for lga_data_list in dataset['LGAs']: # lga_data_list is a list of dictionaries containing lga data
        for lga_data in lga_data_list: 
            lga = Lga(
                state_id=lga_data['state_id'],
                lgas=lga_data['lgas'],
                state=lga_data['state'],
                senatorial_district=lga_data['senatorial_district'],
                area=lga_data['area'],
                population=lga_data['population'],
                headquarters=lga_data['headquarters'],
                description=lga_data['description'],
                created_date=lga_data['created_by'],
                created_by=lga_data['created_at'],
                landmass=lga_data['landmass'],
                borders=lga_data['borders'],
            )
            db.session.add(lga)


        # Load other data models based on your dataset structure and relationships

    db.session.commit()
