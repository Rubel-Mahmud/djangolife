from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=200)
    password = forms.CharField(label='password', max_length=30, widget=forms.PasswordInput)

    def authenticate(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']

        return authenticate(username=username, password=password)

