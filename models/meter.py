from db import db
from models.logindata import Logindata

class Meter(db.Model):
    __tablename__ = 'meters'

    id = db.Column(db.Integer, primary_key=True)
    import_id = db.Column(db.String(32))
    meter_id = db.Column(db.String(32))
    extras = db.Column(db.String(128))
    disabled = db.Column(db.Boolean())

    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))
    task = db.relationship('Task')

    logindata_id = db.Column(db.Integer, db.ForeignKey('logindatas.id'))
    logindata = db.relationship('Logindata')

    readings = db.relationship('Reading')

    statuscode_id = db.Column(db.Integer, db.ForeignKey('statuscodes.id'))
    statuscode = db.relationship('Statuscode')
    
    def __init__(self, importId, meterId, extras=None):
        self.import_id = importId
        self.meter_id = meterId
        self.extras = extras

    def __str__(self):
        return 'Import id: ' + self.meter_id

    def getGrabber(self):
        return self.grabber

    def json(self):
        return {'id' : self.id, 'meter_id' : self.meter_id, 'import_id' : self.import_id, 'extras' : self.extras, 'disabled' : self.disabled, 'task_id' : self.task_id}

    def find_by_id(cls, id):
        return Meter.query.filter_by(id=id).first()

    def belongs_to_task(cls, task_id):
        return Meter.query.filter_by(task_id=task_id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def setTask(self, task_id):
        self.task_id = task_id

    def setLogindata(self, logindata_id):
        self.logindata = Logindata.find_by_id(logindata_id)


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def find_all(cls):
        return Meter.query.all()