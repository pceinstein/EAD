import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # aceita conexão
        self.accept()
    
    def diconnect(self, close_code):
        pass

    # recebe uma mensagem do WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # envia a mensagem para o WebSocket
        self.send(text_data=json.dumps({'message': message}))