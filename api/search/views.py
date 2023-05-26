import json
from flask import Flask, request
from flask_restx import Api, Resource, fields, Namespace
from ..utils.utils import db
from ..models.users import User
from http import HTTPStatus
from ..models.data import Region, State, Lga, City, Area




search_namespace = Namespace('search', description = 'Search related operations')


def load_dataset():
    with open('dataset.py', 'r') as file:
        dataset = json.load(file)

    for region_data in dataset['Region']:
        region = Region(name=region_data['name'])
        db.session.add(region)

        # Load other data models based on your dataset structure and relationships

    db.session.commit()







@search_namespace.route('/regions')
class AddRegions(Resource):
    def get(self):
        regions =  Region.query.all()
        return regions, HTTPStatus.OK
    
    # def post(self):
        # regions 