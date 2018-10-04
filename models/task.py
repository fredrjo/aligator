from db import db
from models.grabber import Grabber
from models.importmail import Importmail
from models.meter import Meter
from models.url import Url
from models.status import Statuscode

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    weekday = db.Column(db.Integer())
    hour = db.Column(db.Integer())

    meters = db.relationship('Meter')

    statuscode_id = db.Column(db.Integer, db.ForeignKey('statuscodes.id'))
    statuscode = db.relationship('Statuscode')

    grabber_id = db.Column(db.Integer, db.ForeignKey('grabbers.id'))
    grabber = db.relationship('Grabber')

    url_id = db.Column(db.Integer, db.ForeignKey('urls.id'))
    url = db.relationship('Url')

    importmail_id = db.Column(db.Integer, db.ForeignKey('importmails.id'))
    importmail = db.relationship('Importmail')

    def __init__(self, name, weekday, hour, grabber_id):
        self.name = name
        self.weekday = weekday
        self.hour = hour
        self.grabber_id = grabber_id

    def __str__(self):
        return 'Task: ' + self.name

    def getGrabber(self):
        grabber = Grabber.find_by_id(Grabber.name, self.grabber_id)
        if grabber:
            return grabber
        else:
            return 0

    def getMeters(self):
        #return self.meters
        #return Meter.belongs_to_task(self, self.id)
        return [Meter.json(myInput) for myInput in self.meters]

    def setUrl(self, url_id):
        self.url_id = url_id

    def getUrl(self):
        return Url.find_by_id(Url, 1)

    def getImportmail(self):
        importmail = Importmail.find_by_id(Importmail, 1)
        return importmail

    def json(self):
        return {'id' : self.id, 'name' : self.name, 'grabber' : self.getGrabber().json(), 'importmail' : self.getImportmail().json(), 'url' : self.getUrl().json(), 'meters' : self.getMeters(), 'weekday': self.weekday, 'hour' : self.hour}

    def find_by_id(cls, id):
        return Task.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def find_all(cls):
        return Task.query.all()