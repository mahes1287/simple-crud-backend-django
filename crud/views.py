from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from firebase_auth.permissions import AllowAll
from .serializers import TranslationSerializer
from .models import Translation
from rest_framework.parsers import JSONParser
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


@api_view(["GET"])
def index(request):
    response = {"message": "Hello api", "data": False, "error": False}
    return Response(data=response, status=status.HTTP_200_OK)


@api_view(["GET"])
# @permission_classes((AllowAny,))
def getTranslations(request):
    translation = Translation.objects.all()
    serializer = TranslationSerializer(translation, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getOneTranslation(request, pk):
    try:
        translation = Translation.objects.get(id=pk)
        serializer = TranslationSerializer(translation, many=False)
        newdict = {"error": False, "message": "success"}
        newdict.update(serializer.data)
        return Response(newdict)

    except ObjectDoesNotExist:
        return Response({"message": "Does not exist", "error": True})


@api_view(["POST"])
@parser_classes([JSONParser])
def createTranslation(request):
    data = request.data
    translation = Translation.objects.create(**data)
    serializer = TranslationSerializer(translation, many=False)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["PUT"])
def updateTranslation(request, pk):
    data = request.data
    translation = Translation.objects.get(id=pk)
    print(data)
    serializer = TranslationSerializer(instance=translation, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
@permission_classes((IsAuthenticated,))
def deleteTranslation(request, pk):
    data = request.data
    translation = Translation.objects.get(id=pk)
    translation.delete()
    return Response("translation was deleted")
