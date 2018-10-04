from flask_restful import Resource, reqparse
from models.logindata import Logindata

class Test(Resource):


    @classmethod
    def get(self):
        logindata = Logindata('FRedrik', 'Pass')
        
        return Logindata.__str__(logindata)
