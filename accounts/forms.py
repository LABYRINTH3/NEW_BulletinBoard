from django import forms
from .models import CustomUser

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    # widget=forms.PasswordInput 사용자가 암호를 입력할때 안보이게 하는거

class UserSignupForm(forms.ModelForm):
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'password']

