from django.db import models
from django.contrib.auth.models import User


class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profileImage = models.ImageField(upload_to='images_profile', null=True, blank=True)
    dateOfBirth = models.DateField(null=True, blank=True)
    ocupation = models.CharField(max_length=60, null=True, blank=True)
    organization = models.CharField(max_length=100, null=True, blank=True)
    bio = models.CharField(max_length=400, null=True, blank=True)
    # UserInbox = models.ManyToManyField('blogapp.Message', default=None, blank=True, related_name='user_inbox')
    def __unicode__(self):
        return self.user.username


class Post(models.Model):
    postId = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='posts')
    postDate = models.DateField(null=True)
    text = models.CharField(max_length=500)
    
    media = models.ImageField(upload_to='images_post')
    likers = models.ManyToManyField(User, default=None, blank=True, related_name='post_likes')
    likes = models.IntegerField(null=True)
    @property
    def num_likes(self):
        return self.likers.all().count()

 

class Follower(models.Model):
    user = models.CharField(max_length=200)
    follower = models.CharField(max_length=200)
    chat_room = models.CharField(max_length=100, null=True)

class ChatModel(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_sender')
    # receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_receiver')
    content = models.TextField(blank=True, null=True)
    thread_name = models.CharField(max_length=64,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True) 

class ChatUserModel(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    name = models.TextField(max_length=64,  blank=True,null=True)
    online_status  = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.user.username