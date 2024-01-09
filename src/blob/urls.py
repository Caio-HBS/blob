from django.urls import path

from blob import views

urlpatterns = [
    path("/a", views.homepage, name="home"),
]
