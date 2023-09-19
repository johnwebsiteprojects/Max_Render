from django.urls import re_path

# from . import consumers
from .consumers import ChatConsumer
from . import consumers
from django.conf.urls import url, re_path


websocket_urlpatterns = [
    # url(r"ws/chat/(?P<room_name>\w+)/$", ChatConsumer),
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer.as_asgi()),
    # re_path(r"ws/chat/(?P<room_name>\w+)/$", ChatConsumer),
]
# websocket_urlpatterns = [
#    url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
# ]
# websocket_urlpatterns = [
#     path('ws/rooms/<uri>/', consumers.ChatConsumer),
# ]
# from django.urls import re_path

# from . import consumers

# websocket_urlpatterns = [
#     re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
# ]