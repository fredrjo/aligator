from flask_restful import Resource, reqparse
from models.url import Url

class ApiUrl(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('login_url')
    parser.add_argument('visit_url')
    parser.add_argument('task_id')

    @classmethod
    def get(self, id=None):
        url = Url.find_by_id(self, id)
        if url:
            return url.json()
        return {'message' : 'Logindata not found'}, 404

    @classmethod
    def put(self, id):
        data = ApiUrl.parser.parse_args()
        url = Url.find_by_id(id)
        if url is None:
            url = Url(data['login_url'], data['visit_url'])
        else:
            url.login_url = data['login_url']
            url.visit_url = data['visit_url']
        url.save_to_db()
        return url.json()

    @classmethod
    def delete(self, id):
        url = Url.find_by_id()
        if url:
            url.delete_from_db()

class ApiUrlList(Resource):
    def get(self):
        urls = Url.find_all(Url)
        return {'urls' : [Url.json(myInput) for myInput in urls]}

    def post(self):
        data = ApiUrl.parser.parse_args()
        print('you are here')
        url = Url(data['login_url'], data['visit_url'])
        try:
            url.save_to_db()
        except:
            return {'message' : 'Failed to save'}, 500

        return url.json(), 201
