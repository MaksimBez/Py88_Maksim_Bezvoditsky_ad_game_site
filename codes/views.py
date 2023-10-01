from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from codes.forms import RegistrationCodesForm
from codes.models import UsersCodes
from account.models import Account


class RegistrationCodes(View):

    template_name = 'codes.html'

    def get(self, request):
        form = RegistrationCodesForm()
        user = request.user
        account_id = Account.objects.get(email=user).id
        number_of_codes = UsersCodes.objects.filter(account_id=account_id).count()
        context = {'form': form, 'number_of_codes': number_of_codes}
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegistrationCodesForm(request.POST)
        if form.is_valid():
            user = request.user
            form.save(user)
            return redirect('home')
        context = {'form': form}
        return render(request, self.template_name, context)

"""
Прописать ошибки else
"""
