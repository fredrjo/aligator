from flask_restful import Resource, reqparse
from models.taskrun import Taskrun

class ApiTaskrun(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('task_id')
    parser.add_argument('runtime')
    parser.add_argument('statuscode_id')
    
    @classmethod
    def get(self, id=None):
        taskrun = Taskrun.find_by_id(self, id)
        if url:
            return taskrun.json()
        return {'message' : 'Taskrun not found'}, 404

    @classmethod
    def put(self, id):
        data = ApiTaskrun.parser.parse_args()
        taskrun = Taskrun.find_by_id(id)
        if taskrun is None:
            taskrun = Taskrun(data['task_id'], data['runtime'], data['statuscode_id'])
        else:
            taskrun.task_id = data['task_id']
            taskrun.date_time = data['runtime']
        taskrun.save_to_db()
        return taskrun.json()

    @classmethod
    def delete(self, id):
        taskrun = Taskrun.find_by_id(id)
        if taskrun:
            taskrun.delete_from_db()

class ApiTaskrunList(Resource):
    def get(self):
        taskruns = Taskrun.find_all(Taskrun)
        return {'taskruns' : [Taskrun.json(myInput) for myInput in taskruns]}

    def post(self):
        data = ApiUrl.parser.parse_args()
        print('you are here')
        taskrun = Taskrun(data['task_id'], data['runtime'], data['statuscode_id'])
        try:
            taskrun.save_to_db()
        except:
            return {'message' : 'Failed to save'}, 500

        return taskrunS.json(), 201
