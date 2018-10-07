from flask import Flask
from flask_restful import Api
from flask_cors import CORS

#from models.importmail import Importmail
#from models.task import Task
#from models.grabber import Grabber
#from models.meter import Meter
#from models.alarm import Alarm
#from models.contact import Contact
#from models.handler import Handler
#from models.logindata import Logindata
from models.reading import Reading
from models.status import Statuscode
#from models.url import Url

from resources.test import Test
from resources.api_logindata import ApiLogindata, ApiLogindataList
from resources.api_url import ApiUrl, ApiUrlList
from resources.api_meter import ApiMeter, ApiMeterList
from resources.api_grabber import ApiGrabber, ApiGrabberList
from resources.api_task import ApiTask, ApiTaskList
from resources.api_contact import ApiContact, ApiContactList
from resources.api_importmail import ApiImportmail, ApiImportmailList
from resources.api_alarm import ApiAlarm, ApiAlarmList
from resources.api_taskrun import ApiTaskrun, ApiTaskrunList

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.secret_key = 'rabarbra'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()
api.add_resource(ApiLogindata, '/logindata/<string:id>')
api.add_resource(ApiUrl, '/url/<string:id>')
api.add_resource(ApiMeter, '/meter/<string:id>')
api.add_resource(ApiGrabber, '/grabber/<string:id>')
api.add_resource(ApiTask, '/task/<string:id>')
api.add_resource(ApiTaskrun, '/taskrun/<string:id>')
api.add_resource(ApiAlarm, '/alarm/<string:id>')
api.add_resource(ApiContact, '/contact/<string:id>')
api.add_resource(ApiImportmail, '/importmail/<string:id>')
#api.add_resource(ApiLogindata, '/logindata/<string:username>')
api.add_resource(ApiUrlList, '/urls')
api.add_resource(ApiMeterList, '/meters')
api.add_resource(ApiGrabberList, '/grabbers')
api.add_resource(ApiTaskList, '/tasks')
api.add_resource(ApiTaskrunList, '/taskruns')
api.add_resource(ApiImportmailList, '/importmails')
api.add_resource(ApiLogindataList, '/logindatas')
api.add_resource(ApiAlarmList, '/alarms')
api.add_resource(ApiContactList, '/contacts')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)