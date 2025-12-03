from django.contrib import admin
from .models import Car
admin.site.register(Car)

class CarAdmin(admin.ModelAdmin):
    list_display = ("id", "car_name", "price", "fuel_type")
    search_fields = ("car_name", "fuel_type")
    list_filter = ("fuel_type",)

