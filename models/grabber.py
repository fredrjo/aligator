from models.handler import Handler

class Grabber(Handler):

    def __init__(self, name, handler):
        self.name = name
        self.handler_type = handler

    def __str__(self):
        return self.name +' of type ' + self.handler_type

    