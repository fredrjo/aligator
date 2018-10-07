from db import db

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

    def getStatusName():
        return Statuscode.find_by_id(Statuscode, self.statuscode_id).name

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    def json(self):
        return {'runtime' : self.date_time, 'task' : getTask(), 'statuscode' : self.getStatusName()}

    def find_all(cls):
        return Taskrun.query.all()