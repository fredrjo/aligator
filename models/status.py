from db import db

class Statuscode(db.Model):
    __tablename__ = 'statuscodes'

    id = db.Column(db.Integer, primary_key=True)
    status_code = db.Column(db.String(32))
    message = db.Column(db.String(64))

    taskruns = db.relationship('Taskrun')

    meters = db.relationship('Meter')

    def __init__(self, code, message):
        self.status_code = str(code)
        self.message = message

    def __str__(self):
        return '' + self.status_code + ' : ' + self.message

    def find_by_id(cls, id):
        return Statuscode.query.filter_by(id=id).first()
    