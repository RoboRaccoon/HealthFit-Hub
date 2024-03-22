from django.db import models

# Create your models here.


class Food(models.Model):
    # 1st key = set on model, 2nd key = human readable
    FOOD_GROUPS = {
        "Baked Foods": "Baked Foods",
        "Snacks": "Snacks",
        "Sweets": "Sweets",
        "Vegetables": "Vegetables",
        "American Indian": "American Indian",
        "Restaurant Foods": "Restaurant Foods",
        "Beverages": "Beverages",
        "Fats and Oils": "Fats and Oils",
        "Meats": "Meats",
        "Dairy and Egg Products": "Dairy and Egg Products",
        "Baby Foods": "Baby Foods",
        "Breakfast Cereals": "Breakfast Cereals",
        "Soups and Sauces": "Soups and Sauces",
        "Beans and Lentils": "Beans and Lentils",
        "Fish": "Fish",
        "Fruits": "Fruits",

    }

    name = models.CharField(max_length=200)
    calories = models.IntegerField(default=0)
    foodGroups = models.CharField(max_length=50, choices=FOOD_GROUPS, default='Baked Foods')

    def __str__(self):
        return self.name


class FoodsEatenList(models.Model):
    title = models.CharField(max_length=100, default='Test_List')
    foodEaten = models.ManyToManyField(Food)

    def __str__(self):
        return self.title
