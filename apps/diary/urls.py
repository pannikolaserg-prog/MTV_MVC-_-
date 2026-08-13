from django.urls import path
from .views import EntryListView, EntryDetailView, EntryCreateView, EntryUpdateView, EntryDeleteView, ExportJSONView, ExportCSVView

app_name = 'diary'

urlpatterns = [
    path('', EntryListView.as_view(), name='entry_list'),
    path('create/', EntryCreateView.as_view(), name='entry_create'),
    path('<int:pk>/', EntryDetailView.as_view(), name='entry_detail'),
    path('<int:pk>/update/', EntryUpdateView.as_view(), name='entry_update'),
    path('<int:pk>/delete/', EntryDeleteView.as_view(), name='entry_delete'),
    path('export/json/', ExportJSONView.as_view(), name='export_json'),
    path('export/csv/', ExportCSVView.as_view(), name='export_csv'),
]
