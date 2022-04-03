from django import forms
from .models import *
from django.core.exceptions import ValidationError


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['teams'].empty_label = "Команда не выбрана"

    class Meta:
        model = Drivers
        fields = ['name', 'slug', 'fromCountry', 'wins', 'content', 'photo', 'is_published', 'teams']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return name
