from django.contrib import admin
from myapp.models import *
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'income', 'expense', 'balance', )


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('profile', 'transaction_name', 'amount', 'transaction_type', 'created_at', )


admin.site.register(Profile,ProfileAdmin)
admin.site.register(Transaction,TransactionAdmin)