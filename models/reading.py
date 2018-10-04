from db import db

class Reading(db.Model):
    __tablename__ = 'readings'

    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime(timezone=False))
    value = db.Column(db.Float(precision=4))

    meter_id= db.Column(db.Integer, db.ForeignKey('meters.id'))
    meter = db.relationship('Meter')
    
    def __init__(self, readingTime, readingValue):
        self.date_time = readingTime
        self.value = readingValue

    def __str__(self):
        return datetime.datetime.strftime(self.datetime, '%d-%m-%Y %H:%m:%s')