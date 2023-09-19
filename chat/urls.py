# chat/urls.py
from django.urls import path, re_path

from . import views
import chat
from blogapp.views import chat_room
app_name = 'chat'
urlpatterns = [
    path("", views.index, name="index"),
    # path("<str:room_name>/", views.room, name="room"),
    re_path(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]