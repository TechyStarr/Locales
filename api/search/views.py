import json
from flask import Flask, request
from flask_restx import Api, Resource, fields, Namespace
from ..utils.utils import db
from ..models.users import User
from http import HTTPStatus
from ..models.data import Region, State, Lga, City, Area, load_dataset




search_namespace = Namespace('search', description = 'Search related operations')


@search_namespace.route('/load-dataset')
class LoadDatasetResource(Resource):
    def get(self):
        load_dataset()
        return {'message': 'Dataset loaded successfully'}


@search_namespace.route('/read-dataset')
class readData(Resource):
    def get(self):
        # load_dataset()
        f = open('api/models/dataset.json')
        print(f.read())
        return {'message': 'Dataset loaded successfully'}






@search_namespace.route('/regions')
class AddRegions(Resource):
    def get(self):
        regions =  Region.query.all()
        return regions, HTTPStatus.OK
    
    # def post(self):
        # regions 