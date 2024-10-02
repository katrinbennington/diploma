from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from main.models import Module
from main.serializers import ModuleSerializer


# Create your views here.
class ModuleCreateAPIView(CreateAPIView):
    """LessonCreateAPIView endpoint"""
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ModuleListAPIView(ListAPIView):
    """LessonListAPIView endpoint"""
    serializer_class = ModuleSerializer
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
