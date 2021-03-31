from django.contrib import admin

from .models import Transaction, Wallet


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance')
    list_filter = ('balance',)
    empty_value_display = '-empty-'


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('wallet', 'date', 'summ', 'comment')
    list_filter = ('date',)
    empty_value_display = '-empty-'
