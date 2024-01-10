from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_http_methods

from blob.forms import PostForm, RegistrationForm
from blob.models import Post, Comments


@require_http_methods(["GET"])
def home_view(request):
    """
    TODO: documentation.
    """
    if request.user.is_authenticated:
        posts = Post.objects.exclude(owner=request.user).order_by("-id")[:5]
    posts = Post.objects.order_by("-id")[:5]

    return render(request, "blob/index.html", {"posts": posts})


@require_http_methods(["GET", "POST"])
def login_view(request):
    """
    TODO: documentation.
    """
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("home")
    else:
        form = AuthenticationForm()

    return render(request, "blob/login.html", {"form": form})


def logout_view(request):
    """
    TODO: documentation.
    """
    pass


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
    pass


def post_random_view(request):
    """
    TODO: documentation.
    """
    pass