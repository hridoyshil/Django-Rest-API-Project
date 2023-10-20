from django.urls import path
from .views import *
from django.contrib import admin


urlpatterns = [
    path("first/", firstAPI),
    path("registration/", registrationAPI),
    path("contact/", ContactAPIView.as_view()),
]
