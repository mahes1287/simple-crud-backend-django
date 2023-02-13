import pytest
from rest_framework.test import APIClient
from crud.factories import TranslationFactory

# from django.contrib.auth.models import User
from user.models import User


# from user.models import User
from django.contrib.auth import get_user_model

# User = get_user_model()


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def translations_batch():
    return TranslationFactory.create_batch(10)


@pytest.fixture
def translation_single():
    return TranslationFactory.create()


# user fixtures


# @pytest.fixture
# @pytest.mark.django_db
# def my_user():
#     user = User.objects.create_user(username="bob", password="1X<ISRUkw+tuK")
#     print(user)
#     if not user:
#         raise Exception("something went wrong with the DB!")
#     user2 = user.save()
#     return user2
#     return


# @pytest.fixture
# @pytest.mark.django_db
# def logged_in_client(client, my_user):
#     print(my_user)
#     return client.force_authenticate(my_user)
