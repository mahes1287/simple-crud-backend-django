from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("translations/", views.getTranslations, name="getAllTranslations"),
    path("translations/create", views.createTranslation, name="createTranslation"),
    path("translations/<str:pk>/", views.getOneTranslation, name="getOneTranslation"),
    path(
        "translations/<str:pk>/update",
        views.updateTranslation,
        name="updateTranslation",
    ),
    path(
        "translations/<str:pk>/delete",
        views.deleteTranslation,
        name="deleteTranslation",
    ),
]
