from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="userIndex"),
    path("create/", views.CreateUser, name="createUser"),
    path("all/", views.GetAllUserInfo, name="getAllUserInfo"),
    path("<str:uid>/", views.GetUserInfo, name="getUserInfo"),
]
