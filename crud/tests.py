import pytest
from rest_framework import status
from django.urls import reverse
import json
from .models import Translation
from .serializers import TranslationSerializer


def test_get_traslation_index_api(client):
    url = reverse("index")
    response = client.get(url)
    assert response.status_code == 200
    assert response.data["message"] == "Hello api"


@pytest.mark.django_db
def test_translation_create_batch(translations_batch):
    # test the database has connected by creating objects
    assert Translation.objects.count() == 10


@pytest.mark.django_db
def test_get_single_translation_exist_in_db(client, translation_single):
    id = 1
    url = reverse("getOneTranslation", args=(id,))

    response = client.get(url)

    translations = Translation.objects.get(id=id)
    expected_data = TranslationSerializer(translations, many=False).data

    assert response.status_code == status.HTTP_200_OK
    assert response.data["error"] == False
    assert response.data["message"] == "success"
    assert response.data["data"] == expected_data


@pytest.mark.django_db
def test_get_single_translation_not_exist_in_db(client, translation_single):
    id = 2
    url = reverse("getOneTranslation", args=(id,))
    response = client.get(url)

    try:
        translations = Translation.objects.get(id=id)
        expected_data = TranslationSerializer(translations, many=False).data
    except Translation.DoesNotExist:
        expected_data = None

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data["error"] == True
    assert response.data["data"] == expected_data  # both are None
    assert response.data["message"] == "Does not exist"


@pytest.mark.django_db
def test_get_all_translations(client, translations_batch):
    url = reverse("getAllTranslations")
    response = client.get(url)
    translations = Translation.objects.all()
    expected_data = TranslationSerializer(translations, many=True).data
    assert response.status_code == status.HTTP_200_OK
    assert len(json.loads(response.content)) == 10
    assert response.data == expected_data


@pytest.mark.django_db
def test_post_translation(client):
    data = {"input": "i am input", "output": "output", "fromUser": "Boy Trucker"}
    output_data = {
        "id": 1,
        "input": "i am input",
        "output": "output",
        "fromUser": "Boy Trucker",
    }
    url = reverse("createTranslation")
    response = client.post(url, data, format="json")

    try:
        translations = Translation.objects.get(id=1)
        expected_data = TranslationSerializer(translations, many=False).data
    except Translation.DoesNotExist:
        expected_data = None

    assert response.status_code == status.HTTP_201_CREATED
    assert json.loads(response.content) == expected_data


@pytest.mark.django_db
def test_put_translation(client):
    data = {"input": "i am input", "output": "output", "fromUser": "Boy Trucker"}
    put_data = {
        "id": 1,
        "input": "i am updated input",
        "output": "updated output",
        "fromUser": "Boy Trucker",
    }
    url_post = reverse("createTranslation")
    url_put = reverse("updateTranslation", kwargs={"pk": 1})

    response_post = client.post(url_post, data, format="json")
    response_put = client.put(url_put, put_data, format="json")

    try:
        translations = Translation.objects.get(id=1)
        expected_data = TranslationSerializer(translations, many=False).data
    except Translation.DoesNotExist:
        expected_data = None
    assert response_post.status_code == status.HTTP_201_CREATED
    assert response_put.status_code == status.HTTP_200_OK
    assert json.loads(response_put.content) == expected_data


@pytest.mark.django_db
def test_delete_translation(client, translation_single):
    start = Translation.objects.all().count()
    url = reverse("deleteTranslation", kwargs={"pk": 1})

    response = client.delete(url)
    end = Translation.objects.all().count()
    response_for_already_deleted = client.delete(url)

    try:
        translations = Translation.objects.get(id=1)
        expected_data = TranslationSerializer(translations, many=False).data
    except Translation.DoesNotExist:
        expected_data = None

    assert start == 1
    assert end == 0
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert response_for_already_deleted.status_code == status.HTTP_404_NOT_FOUND


# @pytest.mark.django_db
# def test_with_authenticated_client(client, User):
#     username = "user1"
#     password = "bar"
#     user = User.objects.create_user(username=username, password=password)
#     # Use this:
#     client.force_login(user)
#     # Or this:
#     client.login(username=username, password=password)
#     response = client.get("/private")
#     assert response.content == "Protected Area"


# @pytest.mark.django_db
# def test_sth_with_auth(logged_in_client):
#     response = logged_in_client.get("/api/")
#     assert response.status_code == 200
