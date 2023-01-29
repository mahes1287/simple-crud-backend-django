from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse


class IndexTestCase(APITestCase):
    def test_index_api(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["message"], "Hello api")


class GetTranslationsTestCase(APITestCase):
    def test_translations_list(self):
        pass


class CreateTranslationTestCase(APITestCase):
    def test_create_translation(self):
        pass


class UpdateTranslationTestCase(APITestCase):
    def test_update_translation(self):
        pass


class DeleteTranslationTestCase(APITestCase):
    def test_update_translation(self):
        pass
