from db import db
class Logindata(db.Model):
    __tablename__ = 'logindatas'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45))
    password = db.Column(db.String(45))

    meters = db.relationship('Meter')

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return 'Username: ' + self.username + ', Password: ' + self.password

    def json(self):
        return {'id' : self.id, 'username' : self.username, 'password' : self.password}

    def find_by_id(cls, id):
        return Logindata.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def find_all(cls):
        return Logindata.query.all()

