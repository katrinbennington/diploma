from django.db import models

NULLABLE = {"blank": True, "null": True}


class Module(models.Model):
    """Образовательный модуль"""
    name = models.CharField(max_length=50, verbose_name="Название")
    description = models.CharField(max_length=100, verbose_name="Описание")