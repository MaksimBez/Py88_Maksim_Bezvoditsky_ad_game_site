from django.forms import TextInput
from promocode.models import UserPromocode
from django import forms
from promocode.validators import promocode_validate
from account.models import Account
from promocode.models import UserTransaction
from prize.models import Prize





class RegistrationPromocodeForm(forms.Form):
    promocode = forms.CharField(
        widget=forms.TextInput, max_length=12, label='Промокод', validators=[promocode_validate]
    )


    def save(self, user):
        promocode = self.cleaned_data['promocode']
        account = Account.objects.get(email=user)
        UserPromocode.objects.create(promocode=promocode, account_id=account.id)


class RegistrationTransactionForm(forms.Form):

    def save(self, user, prize_id):
        account = Account.objects.get(email=user)

        UserTransaction.objects.create(account_id=account.id, prize_id=prize_id)
