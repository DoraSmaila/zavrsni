from django.contrib import admin
from .models import *

# Register your models here.

model_list = [Profile, Post, Like, Follower]
admin.site.register(model_list)