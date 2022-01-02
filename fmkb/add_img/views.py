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
from fmkb.add_img.utils import get_extension, check_extension

IMAGE_TYPE = Union[TemporaryUploadedFile, InMemoryUploadedFile]


class ImageViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs) -> Response:
        width = request.data.get('width', None)
        height = request.data.get('height', None)
        image = request.data.get('image', None)
        if image:
            request.data['width'], request.data['height'] = self.modify_image(image, width, height)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def modify_image(self, file: IMAGE_TYPE, width: Union[int, None], height: Union[int, None]) -> tuple:
        buffer = BytesIO()
        if type(file) == TemporaryUploadedFile and check_extension(file.temporary_file_path()):
            im = img.open(file.temporary_file_path())
            if not width or height:
                width, height = im.size
            im.thumbnail((width, height), img.LANCZOS)
            im.save(file.temporary_file_path())
        elif type(file) == InMemoryUploadedFile and check_extension(file.name):
            extension = get_extension(file.name)
            im = img.open(file.file)
            img_ext = list(os.path.splitext(im.filename))[-1]
            if not width or height:
                width, height = im.size
            im.thumbnail((width, height), img.LANCZOS)
            im.save(buffer, format=extension, quality=90)
            file = InMemoryUploadedFile(buffer, 'ImageField', 'image' + img_ext, extension, sys.getsizeof(buffer), None)
        return width, height

