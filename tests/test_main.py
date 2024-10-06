from main.models import Module
from main.serializers import ModuleSerializer, ModuleListSerializer
from django.test import TestCase


def test_moduleserializer_with_model_instance():
    module = Module.objects.create(name="Test Module", description="Test Description")
    serializer = ModuleSerializer(instance=module)
    expected_data = {"name": "Test Module", "description": "Test Description"}
    assert serializer.data == expected_data


# def test_moduleserializer_with_nested_serializer():
#     module = Module.objects.create(name="Test Module", description="Test Description")
#     nested_serializer = ModuleSerializer(instance=module)
#     expected_data = {"name": "Test Module", "description": "Test Description"}
#     assert nested_serializer.data == expected_data
#
#
# def test_moduleserializer_with_custom_fields():
#     module = Module.objects.create(name="Test Module", description="Test Description")
#     serializer = ModuleSerializer(instance=module)
#     expected_data = {"name": "Test Module", "description": "Test Description"}
#     assert serializer.data == expected_data
#

def test_modulelistserializer_with_single_module_instance():
    module = Module.objects.create(name="Test Module", description="Test Description")
    serializer = ModuleListSerializer(instance=module)
    expected_data = {"id": module.id, "name": "Test Module", "description": "Test Description"}
    assert serializer.data == expected_data
    
    
def test_modulelistserializer_with_multiple_module_instances():
    module1 = Module.objects.create(name="Module 1", description="Description 1")
    module2 = Module.objects.create(name="Module 2", description="Description 2")
    modules = Module.objects.all()
    serializer = ModuleListSerializer(instance=modules, many=True)
    expected_data = [
        {"id": module1.id, "name": "Module 1", "description": "Description 1"},
        {"id": module2.id, "name": "Module 2", "description": "Description 2"},
    ]
    assert serializer.data == expected_data    
    
    
def test_modulelistserializer_with_empty_fields():
    module = Module.objects.create(name="Test Module", description="Test Description")
    module.name = ""
    module.description = ""
    module.save()

    serializer = ModuleListSerializer(instance=module)
    expected_data = {"id": module.id, "name": "", "description": ""}
    assert serializer.data == expected_data    
    
    
def test_modulelistserializer_with_input_data():
    input_data = {
        "name": "Test Module",
        "description": "Test Description"
    }
    serializer = ModuleListSerializer(data=input_data)
    serializer.is_valid(raise_exception=True)
    assert serializer.validated_data == input_data    
    
  
def test_modulelistserializer_with_nested_serializer():
    module = Module.objects.create(name="Test Module", description="Test Description")
    nested_serializer = ModuleListSerializer(instance=module)
    expected_data = {"id": module.id, "name": "Test Module", "description": "Test Description"}
    assert nested_serializer.data == expected_data  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
    
    