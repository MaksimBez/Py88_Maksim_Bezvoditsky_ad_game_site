from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from promocode.forms import RegistrationPromocodeForm
from promocode.counter import counter



class RegistrationPromocode(View):

    template_name = 'promocode.html'

    def get(self, request):
        form = RegistrationPromocodeForm()
        user = request.user
        number_of_available_promocodes = counter(user)
        context = {'form': form, 'number_of_available_promocodes': number_of_available_promocodes}
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegistrationPromocodeForm(request.POST)
        user = request.user
        number_of_available_promocodes = counter(user)
        if form.is_valid():
            form.save(user)
            return redirect('promocode')
        context = {'form': form, 'number_of_available_promocodes': number_of_available_promocodes}
        return render(request, self.template_name, context)

"""
Прописать ошибки else
"""
