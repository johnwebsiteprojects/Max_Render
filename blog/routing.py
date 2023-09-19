from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
# import blogapp.routing
import chat.routing
application = ProtocolTypeRouter({
    'websocket' : AuthMiddlewareStack(URLRouter(chat.routing.websocket_urlpatterns))
})
