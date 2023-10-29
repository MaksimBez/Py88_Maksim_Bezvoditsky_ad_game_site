from django.contrib import admin
from . import models
from promocode.models import UserPromocode, UserTransaction
from prize.models import Prize
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.fields import Field


@admin.register(UserPromocode)
class UserPromocodeAdmin(admin.ModelAdmin):
    list_display = ('promocode', 'account',)
    search_fields = ('promocode', 'account__email',)


class UserTransactionResource(resources.ModelResource):
    prize = Field(attribute='prize__prize', column_name='prize')
    account = Field(attribute='account__email', column_name='account')

    class Meta:
        model = UserTransaction
        exclude = ('id',)


@admin.register(UserTransaction)
class UserTransactionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [UserTransactionResource]
    list_display = ('prize', 'account',)
    search_fields = ('prize__prize', 'account__email',)
    list_filter = ('prize',)
