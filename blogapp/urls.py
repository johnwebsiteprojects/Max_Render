from django.urls import include, path
from . import views
from . import api
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PostView.as_view(), name='home'),
    path('register/', views.register, name='signup' ),
    path('signin/', views.user_login, name='login'),
    path('signout/', views.user_logout, name='logout'),
    path('user-profile/', views.user_profile, name='user-profile'),
    path('user-home/', views.main_user_home, name='main-user-home'),
    path('network_list/', views.network_list, name='network-list'),
    path('<str:username>/', views.UserHome.as_view(), name='user-home'),
    path('user-search', views.user_search, name='search-user'),
    path('chat/<str:room_name>/', views.chat_room, name='chat-room'),
    path('api/user/<str:username>/', api.UserList.as_view(), name='user-list'),
    path('api/posts/<int:pk>/', api.PostsList.as_view(), name='post'),
    path('api/post/', api.NewPostList.as_view(), name='new-post'),
    path('like/<int:post_id>/', views.like, name="likes"), 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
