# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, AsyncJsonWebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()

        self.send(text_data=json.dumps({
            'message': 'connected',
        }))

    def receive(self, text_data):
        print(text_data)

    def disconnect(self):
        pass

    def send_notification(self, event):
        data = json.loads(event.get('value'))
        self.send(text_data=json.dumps({'payload': data}))


class NewConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.room_name = "new_consumer"
        self.room_group_name = "new_consumer_group"
        await(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        await self.accept()

        await self.send(text_data=json.dumps({
            'message': 'connected json consumer !!',
        }))

    async def receive(self, text_data):
        print(text_data)
        await self.send(text_data=json.dumps({'status': 'Connected as new consumer'}))

    async def disconnect(self):
        pass

    async def send_notification(self, event):
        data = json.loads(event.get('value'))
        self.send(text_data=json.dumps({'payload': data}))

    async def send_notification(self, event):
        data = json.loads(event.get('value'))
        await self.send(text_data=json.dumps({'payload': data}))