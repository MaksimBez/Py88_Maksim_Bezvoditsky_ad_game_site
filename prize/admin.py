from django.contrib import admin
from prize.models import Prize
from django.contrib.auth.models import Group

admin.site.unregister(Group)


@admin.register(Prize)
class PrizeAdmin(admin.ModelAdmin):
    list_display = ('prize', 'cost', )
    search_fields = ('prize', 'cost', )
