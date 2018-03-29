# chat/consumers.py
from channels.generic.websocket import WebsocketConsumer
import json
import numpy as np
import time

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()



    def disconnect(self, close_code):
        pass
    '''
    when the websocket receives new text data it echoes to the websocket in the javacript side and then the javascript 
    side write the message in the html page 
    '''
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))
