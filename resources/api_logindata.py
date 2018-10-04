from flask_restful import Resource, reqparse
from models.logindata import Logindata

class ApiLogindata(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username')
    parser.add_argument('password')

    @classmethod
    def get(self, id):
        logindata = Logindata.find_by_id(self, id)
        if logindata:
            return logindata.json()
        return {'message' : 'Logindata not found'}, 404

    @classmethod
    def put(self, id):
        logindata = Logindata.find_by_id(id)
        if logindata is None:
            logindata = Logindata(username, password)
        else:
            logindata.username = username
            logindata.password = password
        logindata.save_to_db()
        return logindata.json()

    @classmethod
    def delete(self, username):
        logindata = Logindata.find_by_username()
        if logindata:
            logindata.delete_from_db()

class ApiLogindataList(Resource):
    def get(self):
        logindata = Logindata.find_all(Logindata)
        return {'logindatas' : [Logindata.json(myInput) for myInput in logindata]}

    def post(self):
        data = ApiLogindata.parser.parse_args()
        print('you are here')
        logindata = Logindata(data['username'], data['password'])
        try:
            logindata.save_to_db()
        except:
            return {'message' : 'Failed to save'}, 500

        return logindata.json(), 201

