from io import BytesIO
from PIL import Image as img

from django.test import TestCase, Client
from django.urls import reverse


class TestImageViewSet(TestCase):

    def generate_photo_file(self) -> BytesIO:
        file = BytesIO()
        image = img.new('RGB', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'JPEG')
        file.name = 'test.jpg'
        file.seek(0)
        return file

    def test_image_empty_POST(self) -> None:
        client = Client()
        response = client.post(reverse('image-list'))
        self.assertEqual(response.status_code, 400)

    def test_image_POST(self) -> None:
        client = Client()
        image = self.generate_photo_file()
        response = client.post(reverse('image-list'), {'image': image, 'width': 1000, 'height': 1000})
        self.assertEqual(response.status_code, 201)
