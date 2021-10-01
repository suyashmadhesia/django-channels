import json
from json.decoder import JSONDecodeError
import time
from asgiref.sync import async_to_sync
import channels
from channels.layers import get_channel_layer
from django.shortcuts import render

# Create your views here.
# chat/views.py
from django.shortcuts import render

from chat.models import Notification

async def index(request):
    for i in range(10):
        channel_layer = get_channel_layer()
        data = {"count" : i}
        await (channel_layer.group_send)(
            'new_consumer_group', {
                'type' : 'send_notification',
                'value' : json.dumps(data)
            }
        )
        time.sleep(1)
    return render(request, 'chat/index.html')

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })