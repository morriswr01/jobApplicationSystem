from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    fName = forms.CharField(max_length = 15, required=True)
    lName = forms.CharField(max_length = 15, required=True)

    class Meta:
        fields = ('email', 'password1', 'password2', 'fName', 'lName')
        model = get_user_model()