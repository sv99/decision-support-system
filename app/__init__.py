from flask import Flask
from flask_restplus import Api


app = Flask(__name__)
api = Api(app, title='Decision Support System',
          description='DSS which provides recommendations on solving common '
                      'issues while working with information security systems')
ns = api.namespace('DSS', description='Get your recommendations or enrich system knowledge-base')

from app import routes
