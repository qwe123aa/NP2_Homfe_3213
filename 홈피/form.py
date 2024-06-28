from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from 홈피.models import recipe


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2']

class SignInForm(forms.Form):
    username = forms.CharField(max_length=12)
    password = forms.CharField(widget=forms.PasswordInput)

class RecipeForm(forms.ModelForm):
    class Meta:
        model = recipe
        fields = ['name', 'pic', 'material', 'process']  # 필드 중 author은 제외