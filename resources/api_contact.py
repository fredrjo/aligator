from flask_restful import Resource, reqparse
from models.contact import Contact

class ApiContact(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name')
    parser.add_argument('email')

    @classmethod
    def get(self, id=None):
        contact = Contact.find_by_id(self, id)
        if contact:
            return contact.json()
        return {'message' : 'Contact not found'}, 404

   

    @classmethod
    def put(self, id=None):
        data = ApiContact.parser.parse_args()
        contact = Contact.find_by_id(data['id'])
        if contact is None:
            contact = Contact(data['name'], data['email'])
        else:
            contact.name = data['name']
            contact.email = data['email']
        contact.save_to_db()
        return contact.json()

    @classmethod
    def delete(self, id):
        contact = Contact.find_by_id(id)
        if contact:
            contact.delete_from_db()

class ApiContactList(Resource):
    def get(self):
        contacts = Contact.find_all(Contact)
        return {'contacts' : [Contact.json(myInput) for myInput in contacts]}

    def post(self):
        data = ApiContact.parser.parse_args()
        print('you are here')
        contact = Contact(data['name'], data['email'])
        try:
            contact.save_to_db()
        except:
            return {'message' : 'Failed to save'}, 500

        return contact.json(), 201