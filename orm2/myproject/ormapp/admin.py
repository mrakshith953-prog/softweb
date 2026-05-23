from django.contrib import admin
from .models import FoodDelivery_DB


class FoodDelivery_DBAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'restaurant_name',
        'food_name',
        'quantity',
        'price',
        'customer_name'
    )


admin.site.register(FoodDelivery_DB, FoodDelivery_DBAdmin)