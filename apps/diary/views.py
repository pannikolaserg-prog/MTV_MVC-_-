import csv
import json

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django_filters.views import FilterView

from .filters import DiaryEntryFilter
from .forms import DiaryEntryForm
from .models import DiaryEntry


class EntryListView(LoginRequiredMixin, FilterView):
    model = DiaryEntry
    template_name = 'diary/entry_list.html'
    context_object_name = 'entries'
    filterset_class = DiaryEntryFilter
    paginate_by = 12

    def get_queryset(self):
        return DiaryEntry.objects.filter(user=self.request.user)


class EntryDetailView(LoginRequiredMixin, DetailView):
    model = DiaryEntry
    template_name = 'diary/entry_detail.html'
    context_object_name = 'entry'


class EntryCreateView(LoginRequiredMixin, CreateView):  # <-- ОДИН РАЗ!
    model = DiaryEntry
    form_class = DiaryEntryForm
    template_name = 'diary/entry_create.html'
    success_url = reverse_lazy('diary:entry_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, '✅ Запись создана!')
        return super().form_valid(form)


class EntryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = DiaryEntry
    form_class = DiaryEntryForm
    template_name = 'diary/entry_update.html'
    success_url = reverse_lazy('diary:entry_list')

    def test_func(self):
        entry = self.get_object()
        return self.request.user == entry.user


class EntryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = DiaryEntry
    template_name = 'diary/entry_delete.html'
    success_url = reverse_lazy('diary:entry_list')

    def test_func(self):
        entry = self.get_object()
        return self.request.user == entry.user


class ExportJSONView(LoginRequiredMixin, View):
    def get(self, request):
        entries = DiaryEntry.objects.filter(user=request.user)
        data = list(entries.values('title', 'content', 'created_at', 'tags', 'is_public'))
        response = HttpResponse(
            json.dumps(data, ensure_ascii=False, default=str, indent=2),
            content_type='application/json'
        )
        response['Content-Disposition'] = 'attachment; filename="diary_entries.json"'
        return response


class ExportCSVView(LoginRequiredMixin, View):
    def get(self, request):
        entries = DiaryEntry.objects.filter(user=request.user)
        response = HttpResponse(content_type='text/csv; charset=utf-8')
        response['Content-Disposition'] = 'attachment; filename="diary_entries.csv"'

        writer = csv.writer(response)
        writer.writerow(['ID', 'Заголовок', 'Содержание', 'Теги', 'Публичная', 'Создано'])

        for entry in entries:
            writer.writerow([
                entry.id,
                entry.title,
                entry.content[:100] + '...' if len(entry.content) > 100 else entry.content,
                ', '.join(entry.tags) if entry.tags else '',
                'Да' if entry.is_public else 'Нет',
                entry.created_at.strftime('%d.%m.%Y %H:%M')
            ])
        return response
