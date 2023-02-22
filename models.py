from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

# Create your models here.

User = get_user_model()

# class User(models.Model):
#     first_name = models.CharField(max_length=30, verbose_name="First name")
#     last_name = models.CharField(max_length=30, verbose_name="Last name")
#     date_of_birth = models.DateField(null=True, blank=True, verbose_name="Date of birth")
#     location = models.CharField(max_length=40, verbose_name="User location")
#     email = models.EmailField()

#     def __str__(self):
#         return self.last_name


class Profile(models.Model):
    
    #profile_name = models.CharField(max_length=30, verbose_name="Profile name")
    #profile_owner = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Profile owner")
    #date_created = models.DateField(null=True, blank=True, verbose_name="Date created")
    #followers = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    id_owner = models.IntegerField()
    avatar = models.ImageField(upload_to='profileimgs', default='defaultimg.png') 
    headerimage = models.ImageField(upload_to='profileimgs', default='header.jpg')
    description = models.TextField(blank=True) 
    location = models.CharField(max_length=100, blank=True)
    firstname = models.CharField(max_length=100, blank=True)
    lastname = models.CharField(max_length=100, blank=True)
    email = models.TextField(blank=True) 

    def __str__(self):
        return self.user.username


class Post(models.Model):

    #content = models.CharField(max_length=300, verbose_name="Content")
    #created_by = models.ForeignKey('Profile', on_delete=models.CASCADE, default=1, verbose_name="Created by")
    #comments = models.ManyToManyField(Comment, verbose_name="Comments")

    post_id = models.UUIDField(primary_key=True, default=uuid.uuid4) #id
    user = models.CharField(max_length=100)
    postimage = models.ImageField(upload_to='postimgs')
    caption = models.TextField()
    time_posted = models.DateTimeField(default=datetime.now) 
    likes = models.IntegerField(default=0) #no_of_likes
    

    def __str__(self):
        return self.user


class Like(models.Model):

    #like_id = models.CharField(max_length=20, verbose_name="Like ID")
    #user_like = models.ForeignKey('Profile', on_delete=models.CASCADE, default=1, verbose_name="Like by")
    #time_liked = models.DateField(null=True, blank=True, verbose_name="Time of liking")

    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username


# class Comment(models.Model):
#     comment_id = models.CharField(max_length=13, verbose_name="Comment ID")
#     content = models.TextField(max_length=50, verbose_name="Content")
#     user_comment = models.ForeignKey('Profile', on_delete=models.CASCADE, default=1, verbose_name="Commented by")
#     time_commented = models.DateField(null=True, blank=True, verbose_name="Time of commenting")

#     def __str__(self):
#         return self.comment_id


class Follower(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user