import requests
import googlemaps
from flask import Flask, request
from flask_restx import Api, Resource, fields, Namespace
from ..utils.utils import db
from ..models.users import User
from http import HTTPStatus
from ..models.data import Region, State, Lga, City, Area




search_namespace = Namespace('search', description = 'Search related operations')


def validate_api_key(api_key):
    # Add your code to validate the API key
    return api_key == 'AIzaSyA7x6Zp7GSt3Nd9pby-eE88B-c4MZq1x5M'

@search_namespace.route('/regions')
class AddRegions(Resource):
    def get(self):
        regions =  Region.query.all()
        return regions, HTTPStatus.OK
    
    # def post(self):
        # regions 