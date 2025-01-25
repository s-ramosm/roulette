from django.contrib import admin
from .models import Roulette
# Register your models here.
class RouletteAdmin(admin.ModelAdmin):
    list_display = ['id', 'state']
    list_filter = ['state']
    search_fields = ['id', 'state']

admin.site.register(Roulette, RouletteAdmin)