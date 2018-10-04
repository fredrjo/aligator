from flask_restful import Resource, reqparse
from models.importmail import Importmail

class ApiImportmail(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name')
    parser.add_argument('email')

    @classmethod
    def get(self, id=None):
        importmail = Importmail.find_by_id(self, id)
        if importmail:
            return importmail.json()
        return {'message' : 'Importmail not found'}, 404

    @classmethod
    def put(self, id):
        data = ApiImportmail.parser.parse_args()
        importmail = Importmail.find_by_id(data['id'])
        if importmail is None:
            importmail = Importmail(data['name'], data['email'])
        else:
            importmail.name = data['name']
            importmail.email = data['email']
        importmail.save_to_db()
        return importmail.json()

    @classmethod
    def delete(self, id):
        importmail = Importmail.find_by_id(id)
        if importmail:
            importmail.delete_from_db()

class ApiImportmailList(Resource):
    def get(self):
        importmails = Importmail.find_all(Importmail)
        return {'importmails' : [Importmail.json(myInput) for myInput in importmails]}

    def post(self):
        data = ApiImportmail.parser.parse_args()
        print('you are here')
        importmail = Importmail(data['name'], data['email'])
        try:
            importmail.save_to_db()
        except:
            return {'message' : 'Failed to save'}, 500

        return importmail.json(), 201
