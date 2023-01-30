from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status
from django.urls import reverse
from .views import (
    getTranslations,
    getOneTranslation,
    createTranslation,
    updateTranslation,
    deleteTranslation,
)
from django.contrib.auth import get_user_model

User = get_user_model()


class IndexTestCase(APITestCase):
    def test_index_api(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Hello api")


class GetTranslationsTestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = getTranslations
        self.url = reverse("getAllTranslations")

    def test_translations_list(self):
        request = self.factory.get(self.url)
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetTranslationsClientTestCase(APITestCase):
    def setUp(self):
        self.url = reverse("getAllTranslations")

    def test_translations_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateTranslationTestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = createTranslation
        self.url = reverse("createTranslation")
        self.user = User.objects.create(
            username="tester",
            email="test@test.com",
            password="password",
        )

    def test_create_translation(self):
        sample_translation = {
            "input": "input1",
            "output": "output1",
            "fromUser": "tester",
        }

        request = self.factory.post(self.url, sample_translation)
        request.user = self.user
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class CreateTranslationClientTestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = createTranslation
        self.url = reverse("createTranslation")
        self.user = User.objects.create(
            username="tester",
            email="test@test.com",
            password="password",
        )

    def test_create_translation(self):
        sample_translation = {
            "input": "input1",
            "output": "output1",
            "fromUser": "tester",
        }

        request = self.factory.post(self.url, sample_translation)
        request.user = self.user
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UpdateTranslationTestCase(APITestCase):
    def test_update_translation(self):
        pass


class DeleteTranslationTestCase(APITestCase):
    def test_update_translation(self):
        pass
