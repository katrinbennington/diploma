from rest_framework.serializers import ModelSerializer

from main.models import Module


class ModuleSerializer(ModelSerializer):
    class Meta:
        model = Module
        fields = "__all__"
