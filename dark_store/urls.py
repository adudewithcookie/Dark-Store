from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet, ShelfViewSet, CustomAuthToken


router = DefaultRouter()
router.register(r'locations', LocationViewSet, basename='location')
router.register(r'shelves', ShelfViewSet, basename='shelf')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', CustomAuthToken.as_view()),
]