from flask_restful import Resource, reqparse
from models.grabber import Grabber

class ApiGrabber(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name')
    parser.add_argument('handler_type')
    parser.add_argument('logindata_id')

    @classmethod
    def get(self, id=None):
        grabber = Grabber.find_by_id(self, id)
        if grabber:
            return grabber.json()
        return {'message' : 'Grabber not found'}, 404

    @classmethod
    def put(self, id):
        data = ApiGrabber.parser.parse_args()
        grabber = Grabber.find_by_id(data['id'])
        if grabber is None:
            grabber = Url(data['name'], data['handler_type'])
        else:
            grabber.name = data['name']
            grabber.handler_type = data['handler_type']
        grabber.save_to_db()
        return grabber.json()

    @classmethod
    def delete(self, id):
        grabber = Grabber.find_by_id()
        if grabber:
            grabber.delete_from_db()

class ApiGrabberList(Resource):
    def get(self):
        grabbers = Grabber.find_all(Grabber)
        return {'grabbers' : [Grabber.json(myInput) for myInput in grabbers]}

    def post(self):
        data = ApiGrabber.parser.parse_args()
        print('you are here')
        grabber = Grabber(data['name'], data['handler_type'])
        try:
            grabber.save_to_db()
        except:
            return {'message' : 'Failed to save'}, 500

        return grabber.json(), 201