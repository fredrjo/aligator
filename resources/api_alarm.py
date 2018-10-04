from flask_restful import Resource, reqparse
from models.alarm import Alarm

class ApiAlarm(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('subject')
    parser.add_argument('alarm_text')
    parser.add_argument('task_id')

    @classmethod
    def get(self, id=None):
        alarm = Alarm.find_by_id(self, id)
        if alarm:
            return alarm.json()
        return {'message' : 'Alarm not found'}, 404

    @classmethod
    def put(self, id):
        data = ApiAlarm.parser.parse_args()
        alarm = Alarm.find_by_id(data['id'])
        if alarm is None:
            alarm = Alarm(data['subject'], data['alarm_text'], data['task_id'])
        else:
            alarm.subject = data['subject']
            alarm.alarm_text = data['alarm_text']
            alarm.task_id = data['task_id']
        alarm.save_to_db()
        return alarm.json()

    @classmethod
    def delete(self, id):
        alarm = alarm.find_by_id(id)
        if alarm:
            alarm.delete_from_db()

class ApiAlarmList(Resource):
    def get(self):
        alarms = Alarm.find_all(Alarm)
        return {'alarms' : [Alarm.json(myInput) for myInput in alarms]}

    def post(self):
        data = ApiAlarm.parser.parse_args()
        print('you are here')
        alarm = Alarm(data['subject'], data['alarm_text'], data['task_id'])
        try:
            alarm.save_to_db()
        except:
            return {'message' : 'Failed to save'}, 500

        return alarm.json(), 201