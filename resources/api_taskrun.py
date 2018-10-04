from flask_restful import Resource, reqparse
from models.taskrun import Taskrun

class ApiTaskrun(Resource):
    
    @classmethod
    def get(self, id=None):
        return {'default' : '111'}