from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TranslationSerializer
from .models import Translation
# Create your views here.

def index(request):
    return HttpResponse("You reached top of Simple Crud App")

@api_view(['GET'])
def getTranslations(request):
    translation = Translation.objects.all()
    serializer = TranslationSerializer(translation, many=True)
    return Response(serializer.data)