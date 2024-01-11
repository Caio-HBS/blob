import random

from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
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
    HTTP Methods allowed: GET.
    """
    posts_count = Post.objects.count()
    if request.user.is_authenticated and posts_count > 5:
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
    HTTP Methods allowed: GET, POST.
    """
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("home")
        else:
            return render(request, 'blob/login.html', {"form": form})
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
    HTTP Methods allowed: POST.
    """
    if request.user.is_authenticated:
        logout(request)

    return redirect("home")


@require_http_methods(["GET", "POST"])
def register_view(request):
    """
    View for registering users.

    Gives the users a way to register on the site through the RegistrationForm.

    URL Call: register/
    HTTP Methods allowed: GET, POST.
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
    View to create new posts.

    Validates new posts and creates them on the db.

    URL Call: post/new-post/
    HTTP Methods allowed: GET, POST.
    """
    if not request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
        else:
            return render(request, 'blob/new-post.html', {"form": form})
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
    View for redirecting the user to a random post.

    Redirects the user.

    URL Call: post/random/
    HTTP Methods allowed: GET.
    """
    max_post_count = Post.objects.count()
    random_post = get_object_or_404(Post, pk=random.randint(1, max_post_count))

    return redirect(reverse("post_detail", kwargs={"slug": random_post.slug}))
