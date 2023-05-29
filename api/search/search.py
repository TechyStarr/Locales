import json
from flask import Flask, request
from flask_restx import Api, Resource, fields, Namespace, abort
from ..utils.utils import db
from ..models.users import User
from http import HTTPStatus
from ..models.data import Region, State, Lga, City, Area, load_dataset
from .serializers import serialized_state
from .serializers import serialized_region


search_ns = Namespace('query', description='Search operations')

state_model = search_ns.model(
    'State', {
        'id': fields.String(required=True),
        'name': fields.String(required=True, description="Course Name"),
        'region': fields.String(required=True, description="Region"),
        'region_id': fields.String(required=True, description="Region ID"),
        'capital': fields.String(required=True, description="Capital"),
        'population': fields.String(required=True, description="Population"),
        'area': fields.String(required=True, description="Area"),
        'postal_code': fields.String(required=True, description="Postal Code"),
        # 'No_of_LGAs': fields.String(required=True, description="No of LGAs"),
        'lgas': fields.String(required=True, description="Local Government Areas"),
    }
)





region_model= search_ns.model(
    'Region', {
        'id': fields.String(required=True),
        'name': fields.String(required=True, description="Course Name"),
        'state': fields.Nested((state_model), required=True, description="States"),
    }
)



@search_ns.route('/')
class QueryStates(Resource):
    @search_ns.doc('search_query')
    @search_ns.marshal_with(state_model)

    def post(self):

        keyword = request.args.get('keyword')  # Get the search keyword from the query parameters
        if keyword:
            # Perform the search query based on the keyword
            # You can customize the search logic based on your requirements
            results = State.query\
                .join(Region)\
                .join(Lga)\
                .filter(
                db.or_(
                    Region.name.ilike(f'%{keyword}%'),  # Search by region name
                    State.name.ilike(f'%{keyword}%'),  # Search by state name
                    State.capital.ilike(f'%{keyword}%'),  # Search by state capital
                    
                    # State.lgas.ilike(f'%{keyword}%')  # Search by local government areas
                )
            ).all()
            
            data = []

            # Serialize the regions
            data+=([serialized_region(region) for region in results])

            # Serialize the states
            data+=([serialized_state(state) for state in results])


            return results, 200
        else:
            return {'message': 'Enter a search keyword'}, 400



# @api.route('/states')
# class StateSearch(Resource):
#     def get(self):
#         keyword = request.args.get('keyword')
#         if keyword:
#             # Perform the search query based on the keyword
#             results = State.query.join(Region).filter(
#                 db.or_(
#                     State.name.ilike(f'%{keyword}%'),
#                     State.capital.ilike(f'%{keyword}%'),
#                     State.local_government_areas.ilike(f'%{keyword}%'),
#                     Region.name.ilike(f'%{keyword}%')  # Include region name in the search
#                 )
#             ).all()

#             # Serialize the search results
#             data = [serialize_state(state) for state in results]

#             return {'results': data}, 200
#         else:
#             return {'message': 'No keyword provided'}, 400












# @search_ns.route('/')
# class QueryRegions(Resource):
#     @search_ns.doc('search_region')
#     @search_ns.marshal_with(region_model)

#     def post(self):

#         keyword = request.args.get('keyword')  # Get the search keyword from the query parameters
#         if keyword:
#             # Perform the search query based on the keyword
#             # You can customize the search logic based on your requirements
#             results = Region.query.filter(
#                 db.or_(
#                     Region.name.ilike(f'%{keyword}%'),  # Search by state name
#                     Region.state.ilike(f'%{keyword}%'),  # Search by state capital
#                     # State.local_government_areas.ilike(f'%{keyword}%')  # Search by local government areas
#                 )
#             ).all()

#             data = [serialized_region(region) for region in results]

#             return results, 200
#         else:
#             return {'message': 'Enter a search keyword'}, 400

