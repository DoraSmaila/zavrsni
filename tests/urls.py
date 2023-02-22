from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import homepage, settings, upload, like, profile, search, signup, userlogin, userlogout


class TestUrls(SimpleTestCase):

    def test_homepage_url_is_resolved(self):
        url = reverse('homepage')
        # print(resolve(url))

        self.assertEquals(resolve(url).func, homepage)

    def test_settings_url_is_resolved(self):
        url = reverse('settings')

        self.assertEquals(resolve(url).func, settings)

    def test_upload_url_is_resolved(self):
        url = reverse('upload')

        self.assertEquals(resolve(url).func, upload)

    def test_like_url_is_resolved(self):
        url = reverse('like')

        self.assertEquals(resolve(url).func, like)

    def test_profile_url_is_resolved(self):
        url = reverse('profile')

        self.assertEquals(resolve(url).func, profile)

    def test_search_url_is_resolved(self):
        url = reverse('search')

        self.assertEquals(resolve(url).func, search)

    def test_signup_url_is_resolved(self):
        url = reverse('signup')

        self.assertEquals(resolve(url).func, signup)

    def test_userlogin_url_is_resolved(self):
        url = reverse('userlogin')

        self.assertEquals(resolve(url).func, userlogin)

    def test_userlogout_url_is_resolved(self):
        url = reverse('userlogout')

        self.assertEquals(resolve(url).func, userlogout)
