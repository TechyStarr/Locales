import json
from flask import Flask, request
from flask_restx import Api, Resource, fields, Namespace, abort
from ..utils.utils import db
from models.users import User
from http import HTTPStatus
from models.data import Region, State, Lga, City, Area, load_dataset
# from .. import cache
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)


cache = Cache(app)

# limiter = Limiter(app, key_func=get_remote_address)



search_namespace = Namespace('search', description = 'Search related operations')

lga_model = search_namespace.model(
    'lga', {
        'id': fields.String(required=True),
        'name': fields.String(required=True, description="LGA Name"),
        'state_id': fields.String(required=True, description="state"),
        'state': fields.String(required=True, description="Region ID"),
        'senatorial_district': fields.String(required=True, description="Capital"),
        'area': fields.String(required=True, description="Area"),
        'population': fields.String(required=True, description="Population"),
        'headquarters': fields.String(required=True, description="Area"),
    }
)




state_model = search_namespace.model(
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
        'lgas': fields.Nested((lga_model), description="Local Government Areas"),
    }
)




region_model= search_namespace.model(
    'Region', {
        'id': fields.String(required=True),
        'name': fields.String(required=True, description="Course Name"),
        'state': fields.Nested((state_model), required=True, description="States"),
    }
)


@search_namespace.route('/load-dataset')
class LoadDatasetResource(Resource):
    def post(self):
        if Region.query.first() or State.query.first() or Lga.query.first():
            abort (400, 'Dataset already loaded')
        load_dataset()
        return {'message': 'Dataset loaded successfully'}
        


@search_namespace.route('/read-dataset')
class readData(Resource):
    def get(self):
        # load_dataset()
        f = open('api/models/dataset.json')
        print(f.read())
        return {'message': 'Dataset loaded successfully'}




# Regions
@search_namespace.route('/regions')
# @cache.cached(timeout=60)  # Cache the response for 60 seconds
# @limiter.limit("100/minute")  # Rate limit of 100 requests per minute (adjust as needed)
class Retrieve(Resource):
    @search_namespace.marshal_with(region_model, as_list=True)
    @search_namespace.doc(
        description='Get all Regions',
    )
    def get(self):
        regions = Region.query.all()
        if regions is None:
            return {'message': 'No Region found'}, HTTPStatus.NOT_FOUND

        return regions, HTTPStatus.OK
    

@search_namespace.route('/create')
class Create(Resource):
    @search_namespace.expect(region_model)
    @search_namespace.marshal_with(region_model)
    @search_namespace.doc(
        description='Create a new Region',
    )
    def post(self):
        data = search_namespace.payload
        region = Region.query.filter_by(name=data['name']).first()
        if region:
            return {'message': 'Region already exists'}, HTTPStatus.BAD_REQUEST
        region = Region(
            name=data['name']
        )   
        region.save()
        response = {region: region, 'message': 'Region created successfully'}
        return response, HTTPStatus.CREATED
    


@search_namespace.route('/update-region/<string:region_id>')
class Update(Resource): 
    @search_namespace.marshal_with(region_model)
    @search_namespace.doc(
        description='Get a Region by ID',
    )
    def patch(self, region_id):
        region = Region.query.filter_by(id=region_id).first()
        if not region:
            return {'message': 'Region not found'}, HTTPStatus.NOT_FOUND
        return region, HTTPStatus.OK



# retrieve data under a region
@search_namespace.route('/regions/<string:region_id>/states')
class Retrieve(Resource):
    @search_namespace.marshal_with(state_model, as_list=True)
    @search_namespace.doc(
        description='Get all States under a Region',
    )
    def get(self, region_id):
        states = State.query.filter_by(region_id=region_id).all()
        if states is None:
            return {'message': 'No State found'}, HTTPStatus.NOT_FOUND

        return states, HTTPStatus.OK
    





# States
@search_namespace.route('/states')
class SearchResource(Resource):
    @search_namespace.marshal_with(state_model, as_list=True)
    @search_namespace.doc(
        description='Get all States',
    )
    def get(self):
        states = State.query.all()

        return states, HTTPStatus.OK
    

# LGA
@search_namespace.route('/lgas')
class RetrieveResource(Resource):
    @search_namespace.marshal_with(lga_model, as_list=True)
    @search_namespace.doc(
        description='Get all lgas',
    )
    def get(self):
        lga = Lga.query.all()

        return lga, HTTPStatus.OK
    

@search_namespace.route('/lgas/<string:lga_id>')
class Retrieve(Resource):
    @search_namespace.marshal_with(lga_model)
    def get(self, lga_id):
        lga = Lga.query.filter_by(id=lga_id).first()
        if lga is None:
            return {"message": "LGA not found"}, HTTPStatus.NOT_FOUND
        
        return lga, HTTPStatus.FOUND
    


    def patch(self, lga_id):
        data = search_namespace.payload
        lga = Lga.query.filter_by(id=lga_id).first()
        if not lga:
            return {'message': 'LGA not found'}, HTTPStatus.NOT_FOUND
        
        lga.name = data['name']
        lga.state_id = data['state_id']
        lga.senatorial_district = data['senatorial_district']
        lga.area = data['area']
        lga.population = data['population']
        lga.headquarters = data['headquarters']
        return lga, HTTPStatus.OK








