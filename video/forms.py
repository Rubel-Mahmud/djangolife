from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=200)
    password = forms.CharField(label='password', max_length=30)

class RegisterForm(forms.Form):
    username = forms.CharField(label='username', max_length=200)
    password = forms.CharField(label='password', max_length=25)
    email = forms.EmailField()