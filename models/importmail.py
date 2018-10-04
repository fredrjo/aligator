from db import db

class Importmail(db.Model):
    __tablename__ = 'importmails'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    email = db.Column(db.String(45))

    tasks = db.relationship('Task')

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return 'Name: ' + self.name + ', Email: ' + self.email
    
    def json(self):
        return {'id' : self.id, 'name' : self.name, 'email' : self.email}

    def find_by_id(cls, id):
        return Importmail.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def find_all(cls):
        return Importmail.query.all()