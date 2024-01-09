from django.urls import path

from blob import views

urlpatterns = [
    path("", views.homepage, name="home"),
]
