from app import api, ns
from flask_restplus import Resource, fields


input_fields = ns.model('ProblemDescription', {'problemDescription': fields.String})
recommendation = ns.model('Recommendation', {'recommendation': fields.String})
# get_parser.add_argument('problemDescription', type=str,
#                         help='Problem description in log or stdout format', location='form')


@ns.route('/GetRecommendation')
class GetRecommendation(Resource):
    @ns.doc(body=input_fields)
    @ns.response(200, 'Success', recommendation)
    def post(self):
        return {'recommendation': 'Hello world!'}


@ns.route('/ComplementKnowledgeBase')
class ComplementKnowledgeBase(Resource):
    def post(self):
        return 'Ok!'
