from django.shortcuts import render

# Create your views here.
from django.utils.safestring import mark_safe
import json
from blogapp.models import *

def index(request):
    return render(request, "chat/index.html")

def room(request, room_name):
    # user_profile = AppUser.objects.get(user=request.user)
    # if user_profile.profileImage:
    #     image_url = user_profile.profileImage.url
    # else:
    #     image_url = ''
    # following_list=[]
    # followings = Follower.objects.filter(follower=request.user)
    # for following in followings:
    #     following_list.append(following)
    # username = str(request.user)
    # return render(request, "blogapp/inbox.html", {'room_name': room_name, "username": username, 'user_profile': user_profile, 'img_url': image_url, 'following_list': following_list})
    
    return render(request, "chat/room.html", {"room_name": room_name})
    # return render(request, "chat/room.html", {"room_name_json": mark_safe(json.dumps(room_name))})
# from django.shortcuts import render


# def index(request):
#     return render(request, "chat/index.html")


# def room(request, room_name):
#     return render(request, "chat/room.html", {"room_name": room_name})