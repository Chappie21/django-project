from django.contrib import admin
from .models import Dev

# Register your models here.
@admin.register(Dev)
class DevAmdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'country', 'created_at', 'updated_at']
    # list_editable = ['first_name', 'last_name', 'country']
    readonly_fields = ['id', 'created_at', 'updated_at']