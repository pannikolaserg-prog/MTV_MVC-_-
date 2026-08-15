import django_filters

from .models import DiaryEntry


class DiaryEntryFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    created_at = django_filters.DateFromToRangeFilter()
    is_public = django_filters.BooleanFilter()

    class Meta:
        model = DiaryEntry
        fields = ['title', 'is_public', 'created_at']
