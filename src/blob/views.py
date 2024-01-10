import random

from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_http_methods

from blob.forms import PostForm, RegistrationForm
from blob.models import Post, Comments


@require_http_methods(["GET"])
def home_view(request):
    """
    View for the index page.

    Gets the five newest posts from the db to show on the main page.

    URL Call: / 
    """
    if request.user.is_authenticated:
        posts = Post.objects.exclude(owner=request.user).order_by("-id")[:5]
    posts = Post.objects.order_by("-id")[:5]

    return render(request, "blob/index.html", {"posts": posts})


@require_http_methods(["GET", "POST"])
def login_view(request):
    """
    View for loggin in users.

    If the user is already logged in, redirects to home page, otherwise
    validates the form and logs them in.

    URL Call: login/
    """
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("home")
    else:
        form = AuthenticationForm()

    return render(request, "blob/login.html", {"form": form})


@require_http_methods(["GET"])
def logout_view(request):
    """
    View for loggin-out users.

    If the user is logged in, logs out. Otherwise, simply redirects them to
    the login page.

    URL Call: logout/
    """
    if request.user.is_authenticated:
        logout(request)

    return redirect("home")


@require_http_methods(["GET", "POST"])
def register_view(request):
    """
    TODO: documentation.
    """
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = RegistrationForm()

    return render(request, "blob/register.html", {"form": form})


@require_http_methods(["GET", "POST"])
def new_post_view(request):
    """
    TODO: documentation.
    """
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()

    return render(request, "blob/new-post.html", {"form": form})


@require_http_methods(["GET", "POST"])
def post_detail_view(request, slug):
    """
    TODO: documentation.
    """
    # TODO: new comment form and validation.
    # TODO: user can delete post.
    # TODO: user can delete comment.
    return

@require_http_methods(["GET"])
def post_random_view(request):
    """
    TODO: documentation.
    """
    max_post_count = Post.objects.count()
    random_post = Post.objects.get(id=random.randint(1, max_post_count))
    
    return redirect(reverse("post_detail", kwargs={"slug": random_post.slug}))
