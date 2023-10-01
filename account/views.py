from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login

from account.forms import RegistrationUserForm


class RegistrationUser(View):

    template_name = 'registration/register.html'

    def get(self, request):
        form = RegistrationUserForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegistrationUserForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('home')
        context = {'form': form}
        return render(request, self.template_name, context)

"""
Прописать else - ошибки
"""