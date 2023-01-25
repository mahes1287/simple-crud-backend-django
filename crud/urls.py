from django.urls import path

from . import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('translations', views.getTranslations, name="getAllTranslations"),
    path('translations/create', views.createTranslation, name="createTranslation")
]