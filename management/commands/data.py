from django.db import transaction
from django.core.management.base import BaseCommand
import random

from main.models import *
from main.factory import *

NUM_USER = 200
NUM_PROFILE = 200
NUM_LIKE = 1000
NUM_COMMENT = 500
NUM_POST = 300

class Command(BaseCommand):

    @transaction.atomic
    def handle(self, *args, **kwargs):
        models = [User, Profile, Like, Comment, Post]

        print("Deleting old data")
        print("...")
        for m in models:
            m.objects.all().delete()
        
        print("Writing new data")
        for _ in range(NUM_USER):
            user = UserFactory()

        for _ in range(NUM_PROFILE):
            profile = ProfileFactory()
        
        for _ in range(NUM_LIKE):
            like = LikeFactory()
        
        for _ in range(NUM_COMMENT):
            comment = CommentFactory()

        for _ in range(NUM_POST):
            post = PostFactory()