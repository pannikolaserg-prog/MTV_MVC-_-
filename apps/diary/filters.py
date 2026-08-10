import django_filters
from .models import DiaryEntry

class DiaryEntryFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    tags = django_filters.CharFilter(lookup_expr='icontains')
    created_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = DiaryEntry
        fields = ['title', 'tags', 'is_public', 'created_at']
