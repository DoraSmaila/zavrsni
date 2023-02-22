from django.urls import path
from . import views
#from main.views import UserList, ProfileList, LikeList, CommentList, PostList

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('like', views.like, name='like'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('follower', views.follower, name='follower'),
    path('search', views.search, name='search'),
    path('signup', views.signup, name='signup'),
    path('userlogin', views.userlogin, name='userlogin'),
    path('userlogout', views.userlogout, name='userlogout'),

    # path('user', UserList.as_view()),
    # path('profile', ProfileList.as_view()),
    # path('like', LikeList.as_view()),
    # path('comment', CommentList.as_view()),
    # path('post', PostList.as_view()),
]