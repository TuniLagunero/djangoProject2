from django import forms
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


class ContactForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Username"
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
            "placeholder": "Password"
        }
    ))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Login Invalid")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user
class RegisterForm(forms.Form):
    username = forms.CharField(label='username', widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Username"
        }
    ))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={
            "class": "form-control",
            "placeholder": "Email"
        }
    ))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
            "placeholder": "Password"
        }
    ))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
            "placeholder": "Confirm Password"
        }
    ))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        foo = User.objects.filter(username=username)
        if foo.exists():
            raise forms.ValidationError("Username is already taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        foo = User.objects.filter(email=email)
        if foo.exists():
            raise forms.ValidationError("Email is already taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password2 != password:
            raise forms.ValidationError("Passwords are not match")
        return data


