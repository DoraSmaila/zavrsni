import factory
import factory.fuzzy
from factory.django import DjangoModelFactory
from main.models import *

from django.core.files.base import ContentFile

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    date_of_birth = factory.Faker("date_of_birth")
    location = factory.Faker("city")
    email = factory.Faker("email")

    """ username = factory.Faker("user_name")
    description = factory.Faker("sentence")
    location = factory.Faker("city")

    @factory.post_generation
    def followers(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for follower in extracted:
                self.followers.add(follower)    


    avatar = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.ImageField()._make_data(
                {'width': 1024, 'height': 786}
            ), 'example.jpg'
        )
    ) """


class ProfileFactory(DjangoModelFactory):
    class Meta:
        model = Profile
    
    profile_name = factory.Faker("user_name")
    profile_owner = factory.Iterator(User.objects.all())
    date_created = factory.Faker("date_this_decade")
    
    avatar = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.ImageField()._make_data(
                {'width': 1024, 'height': 786}
            ), 'example.jpg'
        )
    )

    description = factory.Faker("sentence")

    @factory.post_generation
    def followers(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for follower in extracted:
                self.followers.add(follower)



class LikeFactory(DjangoModelFactory):
    class Meta:
        model = Like
    
    like_id = factory.Faker("ean")
    user_like = factory.Iterator(Profile.objects.all())
    time_liked = factory.Faker("date_this_decade")


class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment
    
    comment_id = factory.Faker("ean")
    content = factory.Faker("paragraph")
    #commented_post = factory.Iterator(Post.objects.all())
    user_comment = factory.Iterator(Profile.objects.all())
    time_commented = factory.Faker("date_this_decade")


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post
    
    post_id = factory.Faker("ean")
    content = factory.Faker("paragraphs")
    created_by = factory.Iterator(Profile.objects.all())
    time_posted = factory.Faker("date_this_decade")

    @factory.post_generation
    def likes(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for like in extracted:
                self.likes.add(like)

    @factory.post_generation
    def comments(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for comment in extracted:
                self.comments.add(comment)    
