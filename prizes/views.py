from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from account.models import Account
from codes.models import UsersCodes
from prizes.models import Prizes
from codes.forms import RegistrationTransactionForm
from codes.counter import counter


class SelectingPrizes(View):

    template_name = 'prizes.html'

    def get(self, request):
        prizes = Prizes.objects.all()
        return render(request, self.template_name, context={'prizes': prizes})


    def post(self, request):
        prizes = Prizes.objects.all()
        form = RegistrationTransactionForm(request.POST)
        prize_id = request.POST.get("prize_id")
        prize = Prizes.objects.filter(id=prize_id).get()
        cost_of_prize = int(prize.cost)
        user = request.user
        number_of_available_codes = counter(user)
        if number_of_available_codes >= cost_of_prize:
            form.save(user, prize_id)
            return redirect('prizes')
        return render(request, self.template_name, context={'prizes': prizes})


"""
Прописать ошибки else
"""
