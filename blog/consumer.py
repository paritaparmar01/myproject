# myapp/consumers.py

import json
from channels.generic.websocket import WebsocketConsumer

class DashboardConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass
    

    def receive(self, text_data):
        data = json.loads(text_data)
        # Process incoming data here if needed
        self.send(text_data=json.dumps({
            'message': data  # Sending back received data for now
        }))
