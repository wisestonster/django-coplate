from django import forms
from .models import User


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["nickname"]

# 으악 들여쓰기 문제였다.
    def signup(self, request, user):
        user.nickname = self.cleaned_data['nickname']
        user.save()
