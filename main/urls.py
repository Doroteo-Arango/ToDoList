# Define paths to each web-page
from django.urls import path

from . import views

# If we get into this app, and we're in the homepage, go to views.index page & this is called "index"
urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view"),
]