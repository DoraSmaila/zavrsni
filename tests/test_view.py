from django.test import TestCase, Client
from django.urls import reverse
from main.models import Profile, Post, Like, Follower


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.homepage_url = reverse('homepage')
        self.profile_url = reverse('profile')
        self.settings_url = reverse('settings')
        self.search_url = reverse('search')
        self.signup_url = reverse('signup')
        self.userlogin_url = reverse('userlogin')
        self.like_list_url = reverse('like_list')

        self.profile = Profile.objects.create(
            user= "TestUser",
            id_owner= "TestID_owner",
            avatar = "TestAvatar",
            description = "TestDescription",
            loaction = "TestLoaction"
        )
        self.post = Post.objects.create(
            post_id = "TestID",
            user= "TestUser",
            postimage = "",
            caption = "TestCaption",
            time_posted = "TestTime",
            likes = "TestLikes"
        )
        self.like = Like.objects.create(
            post_id = "TestID",
            username= "TestUsername",
          
        )

    def test_project_homepage_GET(self):
        client = Client()

        response = client.get(self.homepage_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_project_profile_GET(self):
        client = Client()

        response = client.get(self.profile_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_project_settings_GET(self):
        client = Client()

        response = client.get(self.settings_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'settings.html')

    def test_project_search_GET(self):
        client = Client()

        response = client.get(self.search_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')

    def test_project_signup_GET(self):
        client = Client()

        response = client.get(self.signup_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_project_userlogin_GET(self):
        client = Client()

        response = client.get(self.userlogin_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'userlogin.html')


    def test_project_like_list_GET(self):
        client = Client()

        response = client.get(self.like_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/like_list.html')


    