import os
import firebase_admin
from django.contrib.auth import get_user_model
from firebase_admin import auth, credentials
from rest_framework.authentication import BaseAuthentication

from .exceptions import FirebaseAuthException, InvalidToken, TokenNotFound

from dotenv import load_dotenv

load_dotenv()

config = {
    "type": "service_account",
    "project_id": str(os.getenv("PROJECT_ID")),
    "private_key_id": str(os.getenv("PRIVATE_KEY_ID")),
    "private_key": str(os.getenv("PRIVATE_KEY")),
    "client_email": str(os.getenv("CLIENT_EMAIL")),
    "client_id": str(os.getenv("CLIENT_ID")),
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": str(os.getenv("CLIENT_X509_CERT_URL")),
}

cred = credentials.Certificate(config)

app = firebase_admin.initialize_app(cred)


class FirebaseAuthentication(BaseAuthentication):
    def authenticate(self, request):

        auth_header = request.META.get("HTTP_AUTHORIZATION")

        if auth_header == None:
            return None

        token = auth_header.split(" ").pop()

        if token == "null":
            raise TokenNotFound()

        decoded_token = None
        try:
            decoded_token = auth.verify_id_token(token)
        except Exception:
            raise InvalidToken()

        try:
            uid = decoded_token.get("uid")

        except Exception:
            raise FirebaseAuthException()

        User = get_user_model()

        try:
            user, created = User.objects.get_or_create(username=uid)
            print("in authenticate")
            print(user)
            pass
        except Exception as e:
            print("you got a problem", e)
            return None
        return (user, None)
