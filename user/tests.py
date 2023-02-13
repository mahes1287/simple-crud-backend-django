import pytest

from .models import User


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user("Tony Stark", "tstark@avenegers.com", "jarvis")
    assert User.objects.count() == 1

