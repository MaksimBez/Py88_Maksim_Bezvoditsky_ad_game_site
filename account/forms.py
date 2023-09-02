from django.forms import TextInput, PasswordInput
from account.models import User, Account
from django import forms
from django.contrib.auth.hashers import make_password
from django.forms.forms import BaseForm


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

    def clean(self):
        super().clean()
        form_data = self.cleaned_data
        if form_data['password1'] != form_data['password2']:
            self._errors["password2"] = ["Password do not match"]
            del form_data['password1']
        return form_data

    def save(self):
        name = self.cleaned_data['name']
        surname = self.cleaned_data['surname']
        father_name = self.cleaned_data['father_name']
        phone = self.cleaned_data['phone']
        email = self.cleaned_data['email']
        password = make_password(self.cleaned_data['password1'])

        account = Account.objects.create_user(email=email, password=password)
        User.objects.create(name=name, surname=surname, father_name=father_name, phone=phone, account_id=account.id)
