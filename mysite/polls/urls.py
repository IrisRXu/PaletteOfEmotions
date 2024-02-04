from django.urls import path

from . import views
from django.http import HttpResponse
from .models import Question
from django.urls import path

# name for the url
app_name = "polls"

urlpatterns = [
    path("generated/", views.generate_image_page, name="generated"),
    path("input/", views.user_input, name="input"),
    path("", views.IndexView.as_view(), name="index"),
]
