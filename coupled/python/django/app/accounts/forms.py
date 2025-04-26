from django import forms

from .models import User


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=64, widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=64, widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=64, widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("User already exists!")

        return email

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("password") != cleaned.get("confirm"):
            self.add_error(field="confirm", error="Passwords do not match")

        return cleaned
