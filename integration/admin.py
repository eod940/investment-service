from django.contrib import admin

# Register your models here.
from integration.models import Account, User, Stock, Holdings, Transfer


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    pass


@admin.register(Holdings)
class HoldingsAdmin(admin.ModelAdmin):
    pass


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    pass

