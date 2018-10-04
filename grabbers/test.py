from models.grabber import Grabber
import time
class TestGrabber(Grabber):
    def login(cls):
        print('Login...')
        time.sleep(5)
        print('Login successful')