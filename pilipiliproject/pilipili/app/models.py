from django.db import models

# Create your models here.
class CreateUpdate(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True

class User(CreateUpdate):
    #user_id,user_password
    user_id = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)
    user_email = models.EmailField()

class Post(CreateUpdate):
    #post_title,author_id,content,post_type
    post_title = models.CharField(max_length=50)
    author_id=models.CharField(max_length=20,default='')
    content=models.CharField(max_length=500,default='')
    post_type=models.SmallIntegerField(default='0')

class Comment(CreateUpdate):
   #user_id,post_id,comment
    user_id=models.CharField(max_length=20)
    post_id = models.PositiveIntegerField()
    comment=models.TextField(default='')

class Collection(CreateUpdate):
    #user_id,post_id,post_url,tag
    user_id = models.CharField(max_length=20)
    post_id = models.PositiveIntegerField()
    url =models.CharField(max_length=200)
    tag=models.CharField(max_length=20)

class Bulletscreen(CreateUpdate):
    #video_id,uesr_id,bulletscreen_time,bulletscreen_size,bulletscreen_color,bulletscreen_loc,bulletscreen
    video_id= models.PositiveIntegerField()
    uesr_id=models.CharField(max_length=20)
    bulletscreen_time= models.DateTimeField(auto_now=False)
    bulletscreen_size=models.SmallIntegerField()
    bulletscreen_color=models.SmallIntegerField()
    bulletscreen_loc=models.IntegerField()
    bulletscreen=models.TextField()

class Friend(CreateUpdate):
    #user_id,friend_id,friend_type
    user_id=models.CharField(max_length=20)
    friend_id=models.CharField(max_length=20)
    friend_type=models.SmallIntegerField()

class Like(CreateUpdate):
    #post_id,user_id
    post_id= models.PositiveIntegerField()
    user_id = models.CharField(max_length=20)