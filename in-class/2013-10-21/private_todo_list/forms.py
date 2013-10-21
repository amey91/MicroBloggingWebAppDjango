from django import forms

from models import User

# Based loosely on django.contrib.auth.forms.AuthenticationForm
class AuthenticationForm(forms.Form):
    username = forms.CharField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = User.authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Please enter a correct username and password.')

        return self.cleaned_data
