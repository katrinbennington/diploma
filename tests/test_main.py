import unittest
from django.db import models
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from main.models import Module
from main.serializers import ModuleSerializer, ModuleListSerializer
from main.views import ModuleCreateAPIView, ModuleListAPIView, ModuleRetrieveAPIView, ModuleUpdateAPIView, \
    ModuleDestroyAPIView


class ModuleSerializerTestCase(unittest.TestCase):
    def test_module_serializer_fields(self):
        serializer = ModuleSerializer()
        self.assertEqual(serializer.Meta.model, Module)
        self.assertEqual(serializer.Meta.fields, ("name", "description"))


class ModuleListSerializerTestCase(unittest.TestCase):
    def test_module_list_serializer_fields(self):
        serializer = ModuleListSerializer()
        self.assertEqual(serializer.Meta.model, Module)
        self.assertEqual(serializer.Meta.fields, "__all__")


class ModuleTestCase(unittest.TestCase):
    def test_module_fields(self):
        fields = {
            'name': models.CharField,
            'description': models.CharField,
        }
        for field_name, field_class in fields.items():
            self.assertTrue(hasattr(Module, field_name))
            self.assertIsInstance(getattr(Module, field_name), field_class)
            self.assertEqual(getattr(Module, field_name).max_length, 50 if field_name == 'name' else 100)
            self.assertEqual(getattr(Module, field_name).verbose_name, 'Название' if field_name == 'name' else 'Описание')


class ModuleCreateAPIViewTestCase(unittest.TestCase):
    def test_module_create_api_view_attributes(self):
        view = ModuleCreateAPIView()
        self.assertIsInstance(view, CreateAPIView)
        self.assertEqual(view.queryset.model, Module)
        self.assertEqual(view.serializer_class, ModuleSerializer)


class ModuleListAPIViewTestCase(unittest.TestCase):
    def test_module_list_api_view_attributes(self):
        view = ModuleListAPIView()
        self.assertIsInstance(view, ListAPIView)
        self.assertEqual(view.serializer_class, ModuleListSerializer)
        self.assertEqual(view.queryset.model, Module)


class ModuleRetrieveAPIViewTestCase(unittest.TestCase):
    def test_module_retrieve_api_view_attributes(self):
        view = ModuleRetrieveAPIView()
        self.assertIsInstance(view, RetrieveAPIView)
        self.assertEqual(view.serializer_class, ModuleSerializer)
        self.assertEqual(view.queryset.model, Module)


class ModuleUpdateAPIViewTestCase(unittest.TestCase):
    def test_module_update_api_view_attributes(self):
        view = ModuleUpdateAPIView()
        self.assertIsInstance(view, UpdateAPIView)
        self.assertEqual(view.serializer_class, ModuleSerializer)
        self.assertEqual(view.queryset.model, Module)


class ModuleDestroyAPIViewTestCase(unittest.TestCase):
    def test_module_destroy_api_view_attributes(self):
        view = ModuleDestroyAPIView()
        self.assertIsInstance(view, DestroyAPIView)
        self.assertEqual(view.serializer_class, ModuleSerializer)
        self.assertEqual(view.queryset.model, Module)


if __name__ == '__main__':
    unittest.main()
