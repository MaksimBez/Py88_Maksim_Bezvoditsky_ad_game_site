from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from codes.forms import RegistrationCodesForm
from codes.counter import counter



class RegistrationCodes(View):

    template_name = 'codes.html'

    def get(self, request):
        form = RegistrationCodesForm()
        user = request.user
        number_of_available_codes = counter(user)
        context = {'form': form, 'number_of_available_codes': number_of_available_codes}
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegistrationCodesForm(request.POST)
        user = request.user
        number_of_available_codes = counter(user)
        if form.is_valid():
            form.save(user)
            return redirect('codes')
        context = {'form': form, 'number_of_available_codes': number_of_available_codes}
        return render(request, self.template_name, context)

"""
Прописать ошибки else
"""
