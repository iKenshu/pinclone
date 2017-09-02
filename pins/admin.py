from django.contrib import admin

from .models import Pin

# Register your models here.

@admin.register(Pin)
class PinAdmin(admin.ModelAdmin):
    llist_display = ('title',)