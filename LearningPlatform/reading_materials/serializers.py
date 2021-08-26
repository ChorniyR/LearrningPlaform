from reading_materials.models import ReadingMaterial
from rest_framework.serializers import ModelSerializer


class ReadingMaterialSerializer(ModelSerializer):
    class Meta:
        model = ReadingMaterial
        fields = ['id', 'text', 'title',]
