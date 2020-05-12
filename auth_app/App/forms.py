from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('gender', 'nationality')


class ResetPassword(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput())
    conf_password = forms.CharField(widget=forms.PasswordInput())

    def clean_conf_password(self):
        password = self.cleaned_data['password']
        conf_password = self.cleaned_data['conf_password']

        if password != conf_password:
            raise forms.ValidationError('Both password fields should match')
        else:
            return conf_password
