from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from fmkb.add_img import views

router = routers.DefaultRouter()
router.register(r'images', views.ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
