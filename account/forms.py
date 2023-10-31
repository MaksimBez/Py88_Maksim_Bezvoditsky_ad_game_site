import re

from django.forms import TextInput, PasswordInput
from account.models import User, Account
from django import forms
from django.contrib.auth.hashers import make_password
from django.forms.forms import BaseForm
from django.contrib.auth.views import AuthenticationForm as DjangoAuthenticationForm
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from account.utils import send_email_for_verify
from captcha.fields import CaptchaField
from django.core.validators import RegexValidator



class AuthenticationForm(DjangoAuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            if not Account.objects.filter(email=username).exists():
                raise ValidationError('Пользователь к таким email не существует')
            user = Account.objects.filter(email=username).first()
            if user:
                if not user.check_password(password):
                    raise ValidationError('Неверный пароль', code='password')
            self.user_cache = authenticate(
                self.request, username=username, password=password
            )
            if not self.user_cache.email_verify:
                send_email_for_verify(self.request, self.user_cache)
                raise ValidationError(
                    'Email не подтвержден, проверьте вашу почту',
                    code="invalid_login",
                )

            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


class RegistrationUserForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput, max_length=255, label='Имя')
    surname = forms.CharField(
        widget=forms.TextInput, max_length=255, label='Фамилия')
    father_name = forms.CharField(
        widget=forms.TextInput, max_length=255, label='Отчество')
    phone = forms.CharField(
        widget=forms.TextInput, label='Телефон')
    email = forms.EmailField(
        widget=forms.TextInput, label='Email')
    password1 = forms.CharField(
        widget=forms.PasswordInput, max_length=20, label='Пароль')
    password2 = forms.CharField(
        widget=forms.PasswordInput, max_length=20, label='Подтверждение пароля')
    # captcha = CaptchaField()

    def clean(self):
        super().clean()
        form_data = self.cleaned_data
        if not re.match(r'^[a-zA-Z0-9]+$', form_data['password1']):
            raise ValidationError("Пароль должен содержать латинские буквы")
        if form_data['password1'].isalpha():
            raise ValidationError("Пароль должен содержать цифры и заглавные буквы")
        if form_data['password1'] != form_data['password2']:
            self._errors["password2"] = ["Пароли не совпадают"]
            del form_data['password1']
        return form_data

    def save(self):
        name = self.cleaned_data['name']
        surname = self.cleaned_data['surname']
        father_name = self.cleaned_data['father_name']
        phone = self.cleaned_data['phone']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password1']

        account = Account.objects.create_user(email=email, password=password)
        User.objects.create(name=name, surname=surname, father_name=father_name, phone=phone, account_id=account.id)
