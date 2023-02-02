from django.urls import path

from . import views

urlpatterns = [
    path("users/create/", views.UserCreateView.as_view(), name="user_create"),
    path("token/", views.ObtainAuthTokenView.as_view(), name="token"),
]
