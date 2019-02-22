from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()  # automaticly generates urls for viewset
router.register('tags', views.TagViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]
