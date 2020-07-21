from django.contrib import admin

from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "value", "type_order")
    search_fields = ("name", "user__username", "type_order")
    fields = ("name", "user", "description", "value", "type_order")
