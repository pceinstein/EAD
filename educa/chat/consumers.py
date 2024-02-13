import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.id = self.scope['url_route']['kwargs']['course_id']
        self.room_group_name = 'chat_%s' % self.id
        # associa-se ao grupo da sala
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        # aceita conexão
        self.accept()
    
    def diconnect(self, close_code):
        # sai do grupo da sala
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # recebe uma mensagem do WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # envia a mensagem para o grupo da sala
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
            }
        )
    
    # recebe uma mensagem do grupo da sala
    def chat_message(self, event):
        # envia a mensagem para o WebSocket
        self.send(text_data=json.dumps(event))