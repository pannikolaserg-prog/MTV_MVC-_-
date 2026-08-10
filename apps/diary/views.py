from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django_filters.views import FilterView
from .models import DiaryEntry
from .forms import DiaryEntryForm
from .filters import DiaryEntryFilter

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

class EntryCreateView(LoginRequiredMixin, CreateView):
    model = DiaryEntry
    form_class = DiaryEntryForm
    template_name = 'diary/entry_create.html'
    success_url = reverse_lazy('diary:entry_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Запись создана!')
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
