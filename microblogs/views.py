from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm, LogInForm, PostForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User
from .models import Post
from django.contrib.auth.models import User
from django.template.response import TemplateResponse


# Create your views here.
def log_in(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('feed')
        messages.add_message(request, messages.ERROR, "The credentials provided were invalid!")
    form = LogInForm()
    return render(request,'log_in.html',{'form':form})

def log_out(request):
    logout(request)
    return redirect('home')

def feed(request):
    user = request.user
    posts = Post.objects.filter(author=user)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = user
            post.save()

            #text = form.cleaned_data['text']
            return redirect('feed')
    else:
        form = PostForm()
    args={'user':user, 'form':form, 'posts':posts}
    return render(request, 'feed.html', args)

def new_post(request):
    user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = user
            post.save()

            #text = form.cleaned_data['text']
            return redirect('feed')
    else:
        form = PostForm()
    args = {'form':form, 'user':user}
    return render(request, 'new_post.html', args)

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users':users})

def show_user(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'show_user.html', {'user': user})

def home(request):
    return render(request, 'home.html')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('feed')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form':form})
