from rest_framework.serializers import ModelSerializer

from .models import Translation

class TranslationSerializer(ModelSerializer):
    class Meta:
        model = Translation
        fields = "__all__"