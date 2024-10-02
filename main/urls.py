from django.urls import path

from main.apps import MainConfig
from main.views import ModuleCreateAPIView, ModuleListAPIView, ModuleRetrieveAPIView, ModuleUpdateAPIView, \
    ModuleDestroyAPIView

app_name = MainConfig.name

urlpatterns = [
                  path('create/', ModuleCreateAPIView.as_view(), name='module-create'),
                  path('list/', ModuleListAPIView.as_view(), name='module-list'),
                  path('<int:pk>/', ModuleRetrieveAPIView.as_view(), name='module-get'),
                  path('update/<int:pk>/', ModuleUpdateAPIView.as_view(), name='module-update'),
                  path('delete/<int:pk>/', ModuleDestroyAPIView.as_view(), name='module-delete'),
              ]
