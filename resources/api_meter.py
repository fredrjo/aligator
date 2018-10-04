from flask_restful import Resource, reqparse
from models.meter import Meter

class ApiMeter(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('import_id')
    parser.add_argument('meter_id')
    parser.add_argument('extras')
    parser.add_argument('disabled')
    parser.add_argument('task_id')
    parser.add_argument('logindata_id')

    @classmethod
    def get(self, id=None):
        meter = Meter.find_by_id(self, id)
        if meter:
            return meter.json()
        return {'message' : 'Meter not found'}, 404

    @classmethod
    def put(self, id):
        meter = Meter.find_by_id(id)
        if meter is None:
            meter = Meter(data['import_id'], data['meter_id'], data['extras'])
        else:
            meter.meter_id = data['meter_id']
            meter.import_id = data['import_id']
            meter.extras = data['extras']
        meter.save_to_db()
        return meter.json(), 201

    @classmethod
    def delete(self, id):
        meter = Meter.find_by_id()
        if meter:
            meter.delete_from_db()

class ApiMeterList(Resource):
    def get(self):
        meters = Meter.find_all(Meter)
        return {'meters' : [Meter.json(myInput) for myInput in meters]}

    def post(self):
        data = ApiMeter.parser.parse_args()
        print('you are here')
        meter = Meter(data['import_id'], data['meter_id'], data['extras'])
        if data['task_id']:
            meter.setTask(data['task_id'])
        try:
            meter.save_to_db()
        except:
            return {'message' : 'Failed to save'}, 500

        return meter.json(), 201