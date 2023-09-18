from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import blogapp.routing

application = ProtocolTypeRouter({
    'websocket' : AuthMiddlewareStack(URLRouter(blogapp.routing.websocket_urlpatterns))
})
