from django.db import models

# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=200)
    calories = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class FoodsEatenList(models.Model):
    title = models.CharField(max_length=100, default='Test_List')
    foodEaten = models.ManyToManyField(Food)

    def __str__(self):
        return self.title


