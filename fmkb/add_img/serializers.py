from rest_framework import serializers

from fmkb.add_img.models import Image


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['height', 'width', 'image']
