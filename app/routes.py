from app import api, ns
from flask_restplus import Resource


get_parser = api.parser()
get_parser.add_argument('problemDescription', type=str,
                        help='Problem description in log or stdout format', location='form')


@ns.route('/GetRecommendation')
class GetRecommendation(Resource):
    @ns.expect(get_parser)
    def post(self):
        return 'Hello world!'


@ns.route('/ComplementKnowledgeBase')
class ComplementKnowledgeBase(Resource):
    def post(self):
        return 'Ok!'
