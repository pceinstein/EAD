import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from django.utils import timezone

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.id = self.scope['url_route']['kwargs']['course_id']
        self.room_group_name = 'chat_%s' % self.id
        # associa-se ao grupo da sala
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        # aceita conexão
        await self.accept()
    
    async def diconnect(self, close_code):
        # sai do grupo da sala
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # recebe uma mensagem do WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        now = timezone.now()
        # envia a mensagem para o grupo da sala
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': self.user.username,
                'datetime': now.isoformat(),
            }
        )
    
    # recebe uma mensagem do grupo da sala
    async def chat_message(self, event):
        # envia a mensagem para o WebSocket
        await self.send(text_data=json.dumps(event))