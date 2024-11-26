from django.contrib import admin
from .models import Provider
# Register your models here.
 
@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    pass