from django import forms
from .models import CustomUser

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

    # widget=forms.PasswordInput 사용자가 암호를 입력할때 안보이게 하는거

class UserSignupForm(forms.ModelForm):
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    re_Password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 're_Password']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password")
        password2 = cleaned_data.get("re_Password")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다. 다시 입력해주세요.")
