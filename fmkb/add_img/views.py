import os
import sys
from io import BytesIO
from typing import Union

from PIL import Image as img
from django.core.files.uploadedfile import TemporaryUploadedFile, InMemoryUploadedFile
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from fmkb.add_img.models import Image
from fmkb.add_img.serializers import ImageSerializer

IMAGE_TYPE = Union[TemporaryUploadedFile, InMemoryUploadedFile]


class ImageViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs) -> Response:
        image = request.data.get('image', None)
        width = request.data.get('width', None)
        height = request.data.get('height', None)
        if image and width and height:
            self.modify_image(image, int(width), int(height))
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def modify_image(self, file: IMAGE_TYPE, width: int, height: int) -> None:
        buffer = BytesIO()
        if type(file) == TemporaryUploadedFile:
            im = img.open(file.temporary_file_path())
            im.thumbnail((width, height), img.LANCZOS)
            im.save(file.temporary_file_path())
        else:
            im = img.open(file.file)
            img_ext = list(os.path.splitext(im.filename))[-1]
            im.thumbnail((width, height), img.LANCZOS)
            im.save(buffer, format='JPEG', quality=90)
            file = InMemoryUploadedFile(buffer, 'ImageField', 'image' + img_ext, 'JPEG', sys.getsizeof(buffer), None)
