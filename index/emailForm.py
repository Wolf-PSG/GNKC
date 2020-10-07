from django import forms

class emailForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    message = forms.CharField(widget=forms.Textarea, label='Message', max_length=1000)