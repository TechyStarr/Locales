from flask import Flask
from flask_restx import Api, Resource, fields, Namespace
from ..utils.utils import db
from ..models.info import Region, State, Lga




search_namespace = Namespace('search', description = 'Search related operations')



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
    


