from rest_framework.exceptions import APIException
from rest_framework import status


class FirebaseAuthException(APIException):
    status_code = 500
    default_detail = "Firebase auth exception"
    default_code = "firebase_auth"


class TokenNotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Credentials not found, need to login"
    default_code = "token_not_found"


class InvalidToken(APIException):
    status_code = 401
    default_detail = "Invalid Token"
    default_code = "invalid_token"
