from django.db import models

class FoodDelivery_DB(models.Model):
    restaurant_name = models.CharField(max_length=100)
    food_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    customer_name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.food_name