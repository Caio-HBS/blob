from django.urls import path

from blob import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path("post/random/", views.post_random_view, name="post_random_view"),
    path("post/new-post/", views.new_post_view, name="new_post"),
    path("post/<slug:slug>/", views.post_detail_view, name="post_detail"),
]
