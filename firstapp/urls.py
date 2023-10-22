from django.urls import path
from .views import *


urlpatterns = [
    path("first/", firstAPI),
    path("registration/", registrationAPI),
    path("contact/", ContactAPIView.as_view()),
    path("post/", PostCreatePIView.as_view()),
    # path("postlist/", POSTLISTAPIVIEW.as_view()),
    # path("post/<int:id>/", POSTRetrieveAPIVIEW.as_view()),
    # path("post/<int:id>/", POSTupdateAPIVIEW.as_view()),
    path("post/<int:id>/", POSTRetrieveAPIVIEW.as_view()),
]
