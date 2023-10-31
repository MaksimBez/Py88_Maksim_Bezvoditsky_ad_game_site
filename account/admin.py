from django.contrib import admin
from account.models import Account, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'father_name', 'phone', 'account', )
    search_fields = ('account__email',)


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'email_verify',)
    search_fields = ('email',)
    list_filter = ('email_verify',)
