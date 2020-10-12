from django import forms

class loginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=4)
    password = forms.CharField(label='Password', min_length=6)