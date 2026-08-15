from django import forms

from .models import DiaryEntry


class DiaryEntryForm(forms.ModelForm):
    class Meta:
        model = DiaryEntry
        fields = ['title', 'content', 'tags', 'is_public', 'allow_comments']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Теги через запятую'}),
            'is_public': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'allow_comments': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
