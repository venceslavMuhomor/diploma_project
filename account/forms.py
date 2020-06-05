from django import forms
from blog.models import Post
class LoginForm(forms.Form):
    имя_пользователя = forms.CharField()
    пароль = forms.CharField(widget=forms.PasswordInput)

