from django.db import models


class Image(models.Model):
    name = models.CharField(max_length=40)
    image = models.FileField(upload_to='images/')
