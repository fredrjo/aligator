from flask_restful import Resource, reqparse
from models.task import Task
from grabbers.minenergi import MinEnergiGrabber

class ApiTask(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name')
    parser.add_argument('weekday')
    parser.add_argument('hour')
    parser.add_argument('grabber_id')
    parser.add_argument('url_id')
    parser.add_argument('logindata_id')
   # parser.add_argument('status_id')

    @classmethod
    def get(self, id=None):
        task = Task.find_by_id(self, 1)
        newGrabber = task.getGrabber()
        newGrabber.login(newGrabber)
        if task:
            return task.json()
        return {'message' : 'Task not found'}, 404


    @classmethod
    def put(self, id):
        task = Task.find_by_id(id)
        if task is None:
            task = Task(data['name'], data['weekday'], data['hour'], data['grabber_id'])
        else:
            task.name = data['name']
            task.weekday = data['weekday']
            task.hour = data['hour']
            task.grabber_id = data['grabber_id']
        #    task.status_id = data['status_id']
            task.url_id = data['url_id']
        task.save_to_db()
        return task.json(), 201

    @classmethod
    def delete(self, id):
        task = Task.find_by_id()
        if task:
            task.delete_from_db()

class ApiTaskList(Resource):
    def get(self):
        tasks = Task.find_all(Task)
        return {'tasks' : [Task.json(myInput) for myInput in tasks]}

    def post(self):
        data = ApiTask.parser.parse_args()
        print('you are here')
        if (len(data)== 0):
            task = Task('default', 0, 0, 0)
        else:
            task = Task(data['name'], data['weekday'], data['hour'], data['grabber_id'])
        if data['url_id']:
            task.setUrl(data['url_id'])
        try:
            task.save_to_db()
        except:
            return {'message' : 'Failed to save'}, 500

        return {'id' : task.id}, 201