from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Campos que se mostrarán en la lista del admin
    search_fields = ('name',)     # Permitir búsqueda por el campo "name"
    ordering = ('id',)      