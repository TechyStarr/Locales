from flask_restx import Resource, Namespace
from flask import request


auth_namespace = Namespace('auth', description='Authentication related operations')

