from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import EntityViewSet


router = DefaultRouter()
router.register('entities', EntityViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
