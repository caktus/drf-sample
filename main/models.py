from django.db import models


class Thing(models.Model):
    name = models.CharField(max_length=100)
    internal_field = models.IntegerField(default=0)
