from django.shortcuts import render, redirect
from authentication.forms import RegisterForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Post


@login_required(login_url="/login")
def home(request):
    user_posts = Post.objects.filter(user=request.user)
    username = request.user.username if request.user.is_authenticated else None
    return render(
        request, "authentication/home.html", {"posts": user_posts, "username": username}
    )


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("feed")
    else:
        form = PostForm()
    return render(request, "authentication/createpost.html", {"form": form})


def feed(request):
    posts = Post.objects.all().order_by("-created_date")
    return render(request, "authentication/feed.html", {"posts": posts})


def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/home")
    else:
        form = RegisterForm()
    return render(request, "registration/signup.html", {"form": form})
