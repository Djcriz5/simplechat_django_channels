# chat/consumers.py
from channels.generic.websocket import WebsocketConsumer
import json
import numpy as np
import time

x = np.arange(0,np.pi*10,0.1).tolist()
y = np.sin(x).tolist()
counter = 0
graph_size = 100
data_size = len(list(x))
samples = 0
tic = time.time()


def get_graph_data():
    global counter, data_size, graph_size, x, y
    global samples, tic

    # Calculate FPS
    debug = 0
    if debug:
        samples += 1
        if (time.time() - tic) > 2:
            print("Fps"+format(samples / (time.time() - tic)))
            samples = 0
            tic = time.time()

    counter += 1
    if counter > (data_size - graph_size):
        counter = 0

    graph_to_send = json.dumps({
        'x': x[counter:counter + graph_size],
        'y': y[counter:counter + graph_size]
    })
    return graph_to_send


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
        #print("message received:"+text_data)
        data_to_send=get_graph_data()
        ##print(data_to_send)
        self.send(data_to_send)
