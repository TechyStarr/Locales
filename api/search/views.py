import requests
import googlemaps
from flask import Flask, request
from flask_restx import Api, Resource, fields, Namespace
from ..utils.utils import db
from ..models.users import User
from ..models.info import Region, State, Lga, City, Area




search_namespace = Namespace('search', description = 'Search related operations')

places_ns = Namespace('places', description= "Places API")

@search_namespace.route('/search')
class SearchRegions(Resource):
    def get(self):
        query = search_namespace.payload.get('query')

        regions = Region.query.filter(Region.name.ilike(f'%{query}%')).all()
        states = State.query.filter(State.name.ilike(f'%{query}%')).all()
        lgas = Lga.query.filter(Lga.name.ilike(f'%{query}%')).all()

        return {
            'regions': [region.name for region in regions],
            'states': [state.name for state in states],
            'lgas': [lga.name for lga in lgas]
        }, 200


@search_namespace.route('/regions')
class AddRegions(Resource):
    def post(self):

        pass
    




# @search_namespace.route('/')
# class Search(Resource):
#     def get(self):
#         query = request.args.get('query', '')

#         user = User.query.filter(User.username.ilike(f'%{query}%')).all()
#         regions = Region.query.filter(Region.name.ilike(f'%{query}%')).all()
#         cities = City.query.filter(City.name.ilike(f'%{query}%')).all()
#         lgas = Lga.query.filter(Lga.name.ilike(f'%{query}%')).all()
#         areas = Area.query.filter(Area.name.ilike(f'%{query}%')).all()

#         results = {
#             'regions': [region.name for region in regions],
#             'cities': [city.name for city in cities],
#             'lgas': [lga.name for lga in lgas],
#             'areas': [area.name for area in areas]
#         }

#         return {'results': results}


@places_ns.route('/places')
class GeocodeResource(Resource):
    def get(self):
        gmaps = googlemaps.Client(key='AIzaSyD3mJqxMXXjoUYgpKW9ZErj2VRmhP-HNmU')
        address = '1600 Amphitheatre Parkway, Mountain View, CA'
        geocode_result = gmaps.geocode(address)
        

        # Process the geocode_result as per your requirements
        return {'result': geocode_result}


# @search_namespace.route('/maptest')
# class MapTest(Resource):
#     def get(self):
#         api_key = "AIzaSyD3mJqxMXXjoUYgpKW9ZErj2VRmhP-HNmU"
#         address = "Michael Okpara University"

#         # make a request to google maps places API
#         response = requests.get(
#             f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&types=restaurant&name=harbour&key= AIzaSyD3mJqxMXXjoUYgpKW9ZErj2VRmhP-HNmU"
#             )
#         data = response.json

#         # extract data from response
#         if data['status'] == 'OK':
#             location = data['candidates'][0]['geometry']['location']
#             result = {'latitude': location['lat'], 'longitude': location['lng']}
        
#         else:
#             result = {'error': 'Error retrieveing data from the Google Places API'}

#         return result
