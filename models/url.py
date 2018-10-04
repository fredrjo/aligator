from db import db

class Url(db.Model):
    __tablename__ = 'urls'

    id = db.Column(db.Integer, primary_key=True)
    login_url = db.Column(db.String(64))
    visit_url = db.Column(db.String(64))

    tasks = db.relationship('Task')

    def __init__(self, loginUrl, visitUrl):
        self.login_url = loginUrl
        self.visit_url = visitUrl

    def __str__(self):
        return self.login_url

    def json(self):
        return {'id' : self.id, 'login_url' : self.login_url, 'visit_url' : self.visit_url}

    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def find_all(cls):
        return Url.query.all()
