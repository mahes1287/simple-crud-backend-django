from rest_framework.exceptions import APIException


class FirebaseAuthException(APIException):
    status = 500
    default_detail = "Firebase auth exception"
    default_code = "firebase_auth"


class TokenNotFound(APIException):
    status = 401
    default_detail = "Credentials not found, need to login"
    default_code = "token_not_found"


class InvalidToken(APIException):
    status = 401
    default_detail = "Invalid Token"
    default_code = "invalid_token"
