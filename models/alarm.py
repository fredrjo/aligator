from db import db
class Alarm(db.Model):
    __tablename__ = 'alarms'

    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(64))
    alarm_text = db.Column(db.Text())

    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))
    task = db.relationship('Task')

    def __init__(self, subject, log, task_id):
        self.subject = subject
        self.alarm_text = log
        self.task_id = task_id

    def __str__(self):
        return self.subject + '\n' + self.alarm_text

    def json(self):
        return {'id' : self.id, 'subject' : self.subject, 'alarm_text' : self.alarm_text}

    def find_by_id(cls, id):
        return Alarm.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def find_all(cls):
        return Alarm.query.all()
