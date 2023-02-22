from django.test import TestCase
from main.models import Profile, Post, Like, Follower

class Testmodels(TestCase):

    def setUp(self):
        self.profile = Profile.objects.create(
            user= "TestUser",
            id_owner= "TestID_owner",
            avatar = "TestAvatar",
            description = "TestDescription",
            loaction = "TestLoaction"
        )

    def test_profile(self):
        self.assertEquals(self.profile.user, "TestUser")


    
    def setUp(self):
        self.post = Post.objects.create(
            post_id = "TestID",
            user= "TestUser",
            postimage = "",
            caption = "TestCaption",
            time_posted = "TestTime",
            likes = "TestLikes"
        )

    def test_post(self):
        self.assertEquals(self.post.user, "TestUser")


    def setUp(self):
        self.like = Like.objects.create(
            post_id = "TestID",
            username= "TestUsername",
          
        )

    def test_like(self):
        self.assertEquals(self.like.username, "TestUsername")


    def setUp(self):
        self.follower = Follower.objects.create(
            follower = "TestFollower",
            user = "TestUser",
          
        )

    def test_follower(self):
        self.assertEquals(self.follower.user, "TestUsername")