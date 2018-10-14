from db import db
from models.task import Task
from models.status import Statuscode
import datetime

class Taskrun(db.Model):
    __tablename__ = 'taskruns'

    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime(timezone=False))

    statuscode_id = db.Column(db.Integer, db.ForeignKey('statuscodes.id'))
    statuscode = db.relationship('Statuscode')

    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))
    task = db.relationship('Task')

    def __init__(self, task_id, runtime, statuscode):
        self.date_time = runtime
        self.task_id = task_id
        self.statuscode_id = statuscode

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def getTask(self):
        return Task.find_by_id(Task, self.task_id)

    def getTimeAsString(self):
        return datetime.datetime.strftime(self.date_time, 'HH:mm')

    def getStatusName(self):
        return Statuscode.find_by_id(Statuscode, self.statuscode_id).message

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    def json(self):
        return {'runtime' : self.getTimeAsString(), 'task' : self.getTask().name, 'statuscode' : self.getStatusName()}

    def find_all(cls):
        return Taskrun.query.all()