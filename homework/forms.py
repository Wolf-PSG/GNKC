from homework.models import Homework
from django import forms


class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ['title', 'description', 'due']
        widgets = {
            'description': forms.Textarea(),
            'due': forms.DateInput(format=('%m/%d/%Y'), attrs={'type': 'date'}),
        }
