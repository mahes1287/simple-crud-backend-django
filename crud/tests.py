from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse


class IndexTest(APITestCase):
    def test_index_api(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
