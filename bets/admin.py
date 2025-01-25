from django.contrib import admin
from .models import Bet

# Register your models here.
class BetAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'roulette', 'amount', 'winning_amount', 'number', 'color')
    list_filter = ('color', 'roulette', 'user')
    search_fields = ('user__username', 'roulette__id', 'id')
    ordering = ('id',)

admin.site.register(Bet, BetAdmin)