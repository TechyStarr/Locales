import json
from ..utils.utils import db
from flask import Flask




class Region(db.Model):
    __tablename__ = 'regions'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(45), nullable=False, unique=True)
    cities = db.relationship('City', backref='region', lazy=True)

    def __repr__(self):
        return f"<Region {self.name}>"

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)
    

    
    
class State(db.Model):
    __tablename__ = 'states'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(45), nullable=False, unique=True)
    areas = db.relationship('Area', backref='state', lazy=True)

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
    # areas = db.relationship('Area', backref='city', lazy=True)

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

    for region_data in dataset['Region']:
        region = Region(name=region_data['name'])
        db.session.add(region)

        # Load other data models based on your dataset structure and relationships

    db.session.commit()
