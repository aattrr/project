from django.contrib.auth.models import User
from django.db import models


class Property(models.Model):
    """
    Модель свойств
    """
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)


class Entity(models.Model):
    """
    Модель Сущности
    """
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField()
    properties = models.ManyToManyField(Property)
