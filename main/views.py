from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from main.models import Module
from main.serializers import ModuleSerializer, ModuleListSerializer


# Create your views here.
class ModuleCreateAPIView(CreateAPIView):
    """LessonCreateAPIView endpoint"""
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class ModuleListAPIView(ListAPIView):
    """LessonListAPIView endpoint"""
    serializer_class = ModuleListSerializer
    queryset = Module.objects.all()


class ModuleRetrieveAPIView(RetrieveAPIView):
    """LessonRetrieveAPIView endpoint"""
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()


class ModuleUpdateAPIView(UpdateAPIView):
    """LessonUpdateAPIView endpoint"""
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()


class ModuleDestroyAPIView(DestroyAPIView):
    """LessonDestroyAPIView endpoint"""
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
