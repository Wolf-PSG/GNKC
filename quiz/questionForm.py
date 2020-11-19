from django import forms
from django.forms import widgets
from django.forms.fields import ChoiceField
from .models import Question

answerOptions = (
    ('1', 'answer 1'),
    ('2', 'answer 2'),
    ('3', 'answer 3'),
    ('4', 'answer 4'),
)


class questionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'answer_1', 'answer_2', 'answer_3',
                  'answer_4', 'correct_answer', 'image_path']
        widgets = {
            'correct_answer': forms.Select(attrs={'class': 'select_Correct_Answer'}, choices=answerOptions)
        }
