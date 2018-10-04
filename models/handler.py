from db import db

class Handler(db.Model):
    __tablename__ = 'grabbers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    handler_type = db.Column(db.String(12))

    tasks = db.relationship('Task')

    def __init__(self, name, handler):
        self.name = name
        self.handler_type = handler

    def __str__(self):
        return self.name +' of type ' + self.handler_type

    def json(self):
        return {'id' : self.id, 'name' : self.name, 'handler_type' : self.handler_type}

    def find_by_id(cls, id):
        return Handler.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def find_all(cls):
        return Handler.query.all()