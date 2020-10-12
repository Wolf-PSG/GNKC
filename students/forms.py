from django import forms


class loginForm(forms.Form):
    username = forms.CharField(label='username', max_length=15)
    password = forms.CharField(label='password', max_length=30)
