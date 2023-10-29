from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from account.models import Account
from promocode.models import UserPromocode, UserTransaction
from prize.models import Prize
from promocode.forms import RegistrationTransactionForm
from promocode.counter import counter
from django.core.cache import cache


class SelectingPrize(View):

    template_name = 'prize.html'

    def get(self, request):
        prizes = cache.get('prizes')
        if not prizes:
            prizes = Prize.objects.all()
            cache.set('prizes', prizes, 10)

        user = request.user
        number_of_available_promocodes = counter(user)
        return render(request, self.template_name, context={
            'prizes': prizes, 'number_of_available_promocodes': number_of_available_promocodes})


    def post(self, request):
        prizes = Prize.objects.all()
        form = RegistrationTransactionForm(request.POST)
        prize_id = request.POST.get("prize_id")
        prize = Prize.objects.filter(id=prize_id).get()
        cost_of_prize = int(prize.cost)
        user = request.user
        number_of_available_promocodes = counter(user)
        if number_of_available_promocodes >= cost_of_prize:
            form.save(user, prize_id)
            return redirect('prize')
        return render(request, self.template_name, context={
            'prizes': prizes, 'number_of_available_promocodes': number_of_available_promocodes})


class MyPrize(View):
    template_name = 'my_prize.html'

    def get(self, request):
        user = request.user
        account_id = Account.objects.get(email=user).id
        my_prizes = UserTransaction.objects.filter(account_id=account_id).all()
        number_of_available_promocodes = counter(user)
        return render(request, self.template_name, context={
            'my_prizes': my_prizes, 'number_of_available_promocodes': number_of_available_promocodes})

"""
Прописать ошибки else
"""
