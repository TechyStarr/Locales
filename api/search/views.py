import requests
import googlemaps
from flask import Flask, request
from flask_restx import Api, Resource, fields, Namespace
from ..utils.utils import db
from ..models.users import User
from ..models.info import Region, State, Lga, City, Area




search_namespace = Namespace('search', description = 'Search related operations')

places_ns = Namespace('places', description= "Places API")


def validate_api_key(api_key):
    # Add your code to validate the API key
    return api_key == 'AIzaSyA7x6Zp7GSt3Nd9pby-eE88B-c4MZq1x5M'

@search_namespace.route('/regions')
class AddRegions(Resource):
    def post(self):
        pass




@places_ns.route('/places')
class GeocodeResource(Resource):
    
    def get(self):
        #

        gmaps = googlemaps.Client(key='AIzaSyB1Tkl3ER1n1XJ_e_g8FR0Zx5k4KWNo66I')
        address = '1600 Amphitheatre Parkway, Mountain View, CA'
        geocode_result = gmaps.geocode(address)
        

        # Process the geocode_result as per your requirements
        return {'result': geocode_result}

    






