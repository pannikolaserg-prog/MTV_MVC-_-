from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .viewsets import DiaryEntryViewSet

router = DefaultRouter()
router.register(r'entries', DiaryEntryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
