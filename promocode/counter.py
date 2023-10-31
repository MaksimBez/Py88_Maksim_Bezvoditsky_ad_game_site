from promocode.models import UserPromocode, UserTransaction
from account.models import Account
from prize.models import Prize
from django.core.cache import cache


def counter(user):
    account_id = Account.objects.get(email=user).id
    number_of_promocodes = UserPromocode.objects.filter(account_id=account_id).count()
    number_of_transactions = UserTransaction.objects.filter(account_id=account_id).all().select_related('prize')
    number_of_available_promocodes = number_of_promocodes - _sum_of_transaction(number_of_transactions)
    return number_of_available_promocodes


def _sum_of_transaction(number_of_transactions):
    sum_of_transaction: int = 0
    for transaction in number_of_transactions:
        prize_id = transaction.prize_id
        prize = Prize.objects.get(id=prize_id)
        cost_of_prize = int(prize.cost)
        sum_of_transaction += cost_of_prize
    return sum_of_transaction
