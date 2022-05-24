from .models import Idea
from django.forms import ModelForm, TextInput, Textarea


class IdeaForm(ModelForm):
    class Meta:
        model = Idea
        fields = ["moniker", "author", "password", "content"]
        widgets = {
            "moniker": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя пользователя'
            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль'
            }),
            "content": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            })
        }