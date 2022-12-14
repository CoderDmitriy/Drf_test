from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Entity(models.Model):
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField(blank=True, null=True)
    properties = models.ManyToManyField('Property')


class Property(models.Model):
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
