from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, UserViewSet
from .views import register_user

router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user, name='register'),
] 