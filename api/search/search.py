import json
from flask import Flask, request
from flask_restx import Api, Resource, fields, Namespace, abort
from ..utils.utils import db
from ..models.users import User
from http import HTTPStatus
from ..models.data import Region, State, Lga, City, Area, load_dataset

from serializers import serialized_state

search_ns = Namespace('search', description='Search operations')



@search_namespace.route('/')
class Query(Resource):
    @search_namespace.doc('search_query')
    @search_namespace.marshal_with(state_model)

    def post(self):
        query = request.args.get('query') # get the query string from the url


        keyword = request.args.get('keyword')  # Get the search keyword from the query parameters
        if keyword:
            # Perform the search query based on the keyword
            # You can customize the search logic based on your requirements
            results = State.query.filter(
                db.or_(
                    State.name.ilike(f'%{keyword}%'),  # Search by state name
                    State.capital.ilike(f'%{keyword}%'),  # Search by state capital
                    # State.local_government_areas.ilike(f'%{keyword}%')  # Search by local government areas
                )
            ).all()

            # Serialize the search results
            data = []
            for state in results:
                state_data = {
                    'id': state.id,
                    'name': state.name,
                    'region_id': state.region_id,
                    'capital': state.capital,
                    'population': state.population,
                    'area': state.area,
                    'postal_code': state.postal_code,
                    'No_of_LGAs': state.No_of_LGAs,
                    'lgas': state.lgas
                }
                data.append(state_data)

            return results, 200
        else:
            return {'message': 'No keyword provided'}, 400







@api.route('/states')
class StateSearch(Resource):
    def get(self):
        # ... search logic ...

        # Serialize the search results
        data = [serialize_state(state) for state in results]

        return {'results': data}, 200
