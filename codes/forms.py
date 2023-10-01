from django.forms import TextInput
from codes.models import UsersCodes
from django import forms
from codes.validators import code_validate
from account.models import Account




class RegistrationCodesForm(forms.Form):
    code = forms.CharField(
        widget=forms.TextInput, max_length=12, label='Код', validators=[code_validate]
    )


    def save(self, user):
        code = self.cleaned_data['code']
        account = Account.objects.get(email=user)
        UsersCodes.objects.create(code=code, account_id=account.id)
