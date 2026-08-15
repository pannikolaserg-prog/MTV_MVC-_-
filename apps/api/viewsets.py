from rest_framework import viewsets, permissions, filters
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from apps.diary.models import DiaryEntry
from apps.api.serializers import DiaryEntrySerializer


class DiaryEntryViewSet(viewsets.ModelViewSet):
    queryset = DiaryEntry.objects.all()
    serializer_class = DiaryEntrySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['is_public']  # Только is_public, без tags
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
