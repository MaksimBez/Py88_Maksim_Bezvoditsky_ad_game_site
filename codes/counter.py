from codes.models import UsersCodes, UsersTransactions
from account.models import Account


def counter(user):
    account_id = Account.objects.get(email=user).id
    number_of_codes = UsersCodes.objects.filter(account_id=account_id).count()
    number_of_transactions = UsersTransactions.objects.filter(account_id=account_id).count()
    number_of_available_codes = number_of_codes - number_of_transactions
    return number_of_available_codes
