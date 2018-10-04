from db import db

class Taskrun(db.Model):
    __tablename__ = 'taskruns'

    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime(timezone=False))

    statuscode_id = db.Column(db.Integer, db.ForeignKey('statuscodes.id'))
    statuscode = db.relationship('Statuscode')

    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))
    task = db.relationship('Task')

    def __init__():
        pass