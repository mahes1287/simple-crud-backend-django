from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from .serializers import TranslationSerializer
from .models import Translation
from rest_framework.parsers import JSONParser
# Create your views here.

def index(request):
    return HttpResponse("You reached top of Simple Crud App")

@api_view(['GET'])
def getTranslations(request):
    translation = Translation.objects.all()
    serializer = TranslationSerializer(translation, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@parser_classes([JSONParser])
def createTranslation(request):
    data = request.data
    print(data)
    translation = Translation.objects.create(**data)
    serializer = TranslationSerializer(translation, many=False)
    return Response(serializer.data)

# TODO ensure the response data cntain proper status code.
# TODO error handling is pending