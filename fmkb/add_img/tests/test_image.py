from io import BytesIO

from PIL import Image as img
from django.test import TestCase, Client
from django.urls import reverse


class TestImageViewSet(TestCase):

    def generate_photo_file(self, module: str, extension: str) -> BytesIO:
        file = BytesIO()
        image = img.new(module, size=(100, 100), color=(155, 0, 0))
        image.save(file, extension)
        file.name = f'test.{extension}'
        file.seek(0)
        return file

    def test_image_empty_POST(self) -> None:
        client = Client()
        response = client.post(reverse('image-list'))
        self.assertEqual(response.status_code, 400)

    def test_RGB_image_POST(self) -> None:
        client = Client()
        image = self.generate_photo_file('RGB', 'jpeg')
        response = client.post(reverse('image-list'), {'image': image, 'width': 1000, 'height': 1000})
        self.assertEqual(response.status_code, 201)

    def test_RGBA_image_POST(self) -> None:
        client = Client()
        image = self.generate_photo_file('RGBA', 'png')
        response = client.post(reverse('image-list'), {'image': image, 'width': 1000, 'height': 1000})
        self.assertEqual(response.status_code, 201)

    def test_wrong_file_extension_POST(self) -> None:
        client = Client()
        image = self.generate_photo_file('RGB', 'pdf')
        response = client.post(reverse('image-list'), {'image': image, 'width': 1000, 'height': 1000})
        self.assertEqual(response.status_code, 400)
