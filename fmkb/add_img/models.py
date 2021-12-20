from django.db import models


class Image(models.Model):
    image = models.FileField(upload_to='images/')
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
