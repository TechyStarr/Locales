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
    return api_key == 'AIzaSyB1Tkl3ER1n1XJ_e_g8FR0Zx5k4KWNo66I'

@search_namespace.route('/regions')
class AddRegions(Resource):
    def post(self):
        pass




@places_ns.route('/places')
class GeocodeResource(Resource):
    
    def get(self):
        # Test google maps api  with a sample address
        
        # api_key = 'AIzaSyAo5kaSVQUzqwlLCuGwNLiPB_umIGOdtuM'
        # url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&types=restaurant&name=harbour&key=AIzaSyAo5kaSVQUzqwlLCuGwNLiPB_umIGOdtuM"

        # response = requests.get(url)
        # data = response.json()
        # print(data)


        # return {'result': api_key}

        gmaps = googlemaps.Client(key='AIzaSyB1Tkl3ER1n1XJ_e_g8FR0Zx5k4KWNo66I')
        address = '1600 Amphitheatre Parkway, Mountain View, CA'
        geocode_result = gmaps.geocode(address)
        

        # Process the geocode_result as per your requirements
        return {'result': geocode_result}

    






