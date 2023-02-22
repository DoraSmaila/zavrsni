from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
# from django.views.generic import ListView
# from main.models import User, Profile, Like, Comment, Post
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from itertools import chain
import random
from django.shortcuts import get_object_or_404

# Create your views here.

@login_required(login_url='userlogin')
def homepage(request):

    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    following_list = []
    feed = []

    following = Follower.objects.filter(follower=request.user.username)

    for users in following:
        following_list.append(users.user)

    for usernames in following_list:
        feed_list = Post.objects.filter(user=usernames)
        feed.append(feed_list)

    feed_list = list(chain(*feed))

    post_feed = Post.objects.all()

    all_users = User.objects.all()
    user_following_all = []

    for user in following:
        user_list = User.objects.get(username=user.user)
        user_following_all.append(user_list)

    new_suggestions = [x for x in list(all_users) if (x not in list(user_following_all))] #definira sve usere u bazi
    current_user = User.objects.filter(username=request.user.username)
    suggestions_list = [x for x in list(new_suggestions) if (x not in list(current_user))] #definir da nemos pratit sam sebe
    random.shuffle(suggestions_list)

    username_profile = []
    username_profile_list = []

    for users in suggestions_list:
        username_profile.append(users.id)

    for ids in username_profile:
        profile_lists = Profile.objects.filter(id_owner=ids)
        username_profile_list.append(profile_lists)

    suggestions_profile_list = list(chain(*username_profile_list))

    context = { 'user_profile' : user_profile, 'post_feed' : feed_list, 'user_object' : user_object, 'suggestions_profile_list' : suggestions_profile_list[:5]}

    return render(request, 'base.html', context)

@login_required(login_url='userlogin')
def settings(request):

    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        
        if request.FILES.get('profilepicture') == None:

            if request.FILES.get('header') == None:

                profilepicture = user_profile.avatar
                header = user_profile.headerimage
                description = request.POST['description']
                location = request.POST['location']
                firstname=request.POST['firstname']
                lastname=request.POST['lastname']

                user_profile.avatar = profilepicture
                user_profile.headerimage = header
                user_profile.description = description
                user_profile.location = location
                user_profile.firstname=firstname
                user_profile.lastname=lastname
                user_profile.save()


            if request.FILES.get('header') != None:

                profilepicture = user_profile.avatar
                header = request.FILES.get('header')
                description = request.POST['description']
                location = request.POST['location']
                firstname=request.POST['firstname']
                lastname=request.POST['lastname']

                user_profile.avatar = profilepicture
                user_profile.headerimage = header
                user_profile.description = description
                user_profile.location = location
                user_profile.firstname=firstname
                user_profile.lastname=lastname
                user_profile.save()
    

        if request.FILES.get('profilepicture') != None:

            if request.FILES.get('header') == None:

                profilepicture = request.FILES.get('profilepicture')
                header = user_profile.headerimage
                description = request.POST['description']
                location = request.POST['location']
                firstname=request.POST['firstname']
                lastname=request.POST['lastname']

                user_profile.avatar = profilepicture
                user_profile.headerimage = header
                user_profile.description = description
                user_profile.location = location
                user_profile.firstname=firstname
                user_profile.lastname=lastname
                user_profile.save()


            if request.FILES.get('header') != None:

                profilepicture = request.FILES.get('profilepicture')
                header = request.FILES.get('header')
                description = request.POST['description']
                location = request.POST['location']
                firstname=request.POST['firstname']
                lastname=request.POST['lastname']

                user_profile.avatar = profilepicture
                user_profile.headerimage = header
                user_profile.description = description
                user_profile.location = location
                user_profile.firstname=firstname
                user_profile.lastname=lastname
                user_profile.save()
                
            return redirect('settings')


    context = { 'user_profile' : user_profile, 'user_object' : user_object }

    return render(request, 'settings.html', context)

@login_required(login_url='userlogin')
def upload(request):
    

    if request.method == 'POST':
        user = request.user.username
        postimage = request.FILES.get('uploadimage')
        caption = request.POST['caption']

        new_post = Post.objects.create(user=user, postimage=postimage, caption=caption)
        new_post.save()

        return redirect('/')
    
    else:
        return redirect('/')

    return HttpResponse('<h1>Upload view</h1>')


@login_required(login_url='userlogin')
def like(request):
    username = request.user.username
    post_id = request.GET.get('post_id')
    post = Post.objects.get(post_id=post_id)

    filter_likes = Like.objects.filter(post_id=post_id, username=username).first()

    if filter_likes == None:
        new_like = Like.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.likes = post.likes+1
        post.save()
        return redirect('/')
    
    else:
        filter_likes.delete()
        post.likes = post.likes-1
        post.save()
        return redirect('/')


@login_required(login_url='userlogin')
def profile(request, pk):

    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user_posts = Post.objects.filter(user=pk)
    user_posts_num = len(user_posts)

    follower = request.user.username
    user = pk

    if Follower.objects.filter(follower=follower, user=user).first():
        button_text = 'Unfollow'
    
    else:
        button_text = 'Follow'

    user_followers = len(Follower.objects.filter(user=pk))
    user_following = len(Follower.objects.filter(follower=pk))

    context = { 'user_object' : user_object, 'user_profile' : user_profile, 'user_posts' : user_posts, 'user_posts_num' : user_posts_num, 'button_text' : button_text, 'user_followers' : user_followers, 'user_following' : user_following }

    return render(request, 'profile.html', context)


@login_required(login_url='userlogin')
def follower(request):
    
    if request.method == 'POST':
        follower = request.POST['follower']
        user = request.POST['user']

        if Follower.objects.filter(follower=follower, user=user).first():
            delete_follower = Follower.objects.get(follower=follower, user=user)
            delete_follower.delete()
            return redirect('/profile/'+user)
        
        else:
            new_follower = Follower.objects.create(follower=follower, user=user)
            new_follower.save()
            return redirect('/profile/'+user)
    
    else:
        return redirect('/')


@login_required(login_url='userlogin')
def search(request):

    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    if request.method == 'POST':
        username = request.POST['username']
        username_object = User.objects.filter(username__icontains=username)

        username_profile = []
        username_profile_list = []

        for users in username_object:
            username_profile.append(users.id)

        for ids in username_profile:
            profile_lists = Profile.objects.filter(id_owner=ids)
            username_profile_list.append(profile_lists)

        username_profile_list = list(chain(*username_profile_list))

    context = { 'user_object' : user_object, 'user_profile' : user_profile, 'username_profile_list' : username_profile_list }

    return render(request, 'search.html', context)


def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:

            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('signup')

            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('signup')
            
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_owner=user_model.id)
                new_profile.save()
                return redirect('/')

        else:
            messages.info(request, 'Passwords Not Matching')
            return redirect('signup')

    else:
        return render(request, 'signup.html')


def userlogin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        
        else:
            messages.info(request, 'Login failed')
            return redirect('userlogin')
    
    else:
        return render(request, 'userlogin.html')


@login_required(login_url='userlogin')
def userlogout(request):
    auth.logout(request)
    return redirect('userlogin')


# class UserList(ListView):
#     model = User

# class ProfileList(ListView):
#     model = Profile

# class LikeList(ListView):
#     model = Like

# class CommentList(ListView):
#     model = Comment

# class PostList(ListView):
#     model = Post