from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="userIndex"),
    path("<str:uid>/", views.GetUserInfo, name="getUserInfo"),
    path("create", views.CreateUser, name="createUser"),
]

# TODO set things for 404 response for invalid urls
