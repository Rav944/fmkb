import os
from typing import Union
from django.core.files.uploadedfile import TemporaryUploadedFile, InMemoryUploadedFile
from rest_framework import serializers

from fmkb.add_img.models import Image

ALLOWED_IMAGE_EXTENSIONS = ["png", "jpg", "jpeg"]
IMAGE_TYPE = Union[TemporaryUploadedFile, InMemoryUploadedFile]


class ImageSerializer(serializers.HyperlinkedModelSerializer):

    def validate_image(self, img: IMAGE_TYPE) -> IMAGE_TYPE:
        if type(img) == TemporaryUploadedFile:
            file = img.temporary_file_path()
        else:
            file = img.name
        extension = os.path.splitext(file)[1].replace(".", "")
        if extension.lower() in ALLOWED_IMAGE_EXTENSIONS:
            return img
        raise serializers.ValidationError(f'Invalid uploaded file type: {file}', code='invalid')

    class Meta:
        model = Image
        fields = ['height', 'width', 'image']
