# news/forms.py
from django import forms
from .models import NewPost

class NewsForm(forms.ModelForm):
    class Meta:
        model = NewPost
        fields = ['title', 'short_description', 'text']
        labels = {
            'title': 'Заголовок',
            'short_description': 'Краткое описание',
            'text': 'Текст новости',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }