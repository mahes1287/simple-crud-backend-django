from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from .models import User
from rest_framework.parsers import JSONParser
from django.core.exceptions import ObjectDoesNotExist


@api_view(["GET"])
def index():
    response = {"message": "Hello from user app", "data": False, "error": False}
    return Response(data=response, status=status.HTTP_200_OK)


@api_view(["POST"])
@parser_classes([JSONParser])
def CreateUser(request):
    data = request.data
    user = User.objects.create(**data)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def GetUserInfo(request, uid):
    try:
        user = User.objects.get(uid=uid)
        serializer = UserSerializer(user, many=False)
        newdict = {"error": False, "message": "success", "data": serializer.data}
        return Response(newdict, status=status.HTTP_200_OK)

    except ObjectDoesNotExist:
        print("error")
        return Response(
            {"message": "Does not exist", "error": True},
            status=status.HTTP_404_NOT_FOUND,
        )


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def GetAllUserInfo(request):
    try:
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        newdict = {"error": False, "message": "success", "data": serializer.data}
        return Response(newdict, status=status.HTTP_200_OK)

    except ObjectDoesNotExist:
        return Response(
            {"message": "Does not exist", "error": True},
            status=status.HTTP_404_NOT_FOUND,
        )
