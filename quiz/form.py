from django import forms
from .models import Quiz


class quizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'level', 'classes', 'image_path']
