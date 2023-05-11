from flask_restx import Resource, Namespace
from flask import request
from http import HTTPStatus


auth_namespace = Namespace('auth', description='Authentication related operations')


class test(Resource):

    def post():
        response = {
            "message": "Hello World!"
        }

        return response, HTTPStatus.ACCEPTED


