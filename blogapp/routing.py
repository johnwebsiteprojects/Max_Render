# # from django.urls import re_path
# # from . import consumers

# # websocket_urlpatterns = [
# #     re_path(r'ws/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi())
# # ]


# from django.urls import re_path

# # from . import consumers

# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# import chat.routing

# application = ProtocolTypeRouter({
#     'websocket': AuthMiddlewareStack(
#         URLRouter(
#             chat.routing.websocket_urlpatterns
#         )
#     )
# })