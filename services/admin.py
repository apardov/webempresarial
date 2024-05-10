from django.contrib import admin
from .models import Service


# Register your models here.

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    # sirve para mostrar campos en modo lectura
    readonly_fields = ('created', 'updated')
