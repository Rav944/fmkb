from rest_framework import viewsets, mixins

from fmkb.add_img.models import Image
from fmkb.add_img.serializers import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
