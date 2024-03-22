# Create your models here.
from django.db import models
from django import forms


class Profile(models.Model):
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    gender = models.CharField(max_length=20, choices=[('male', 'Male'), ('female', 'Female'),
                                                      ('prefer_not_to_say', 'Prefer not to say')])
    allergy = models.CharField(max_length=100, blank=True)
    body_fat = models.CharField(max_length=20, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
    current_goal = models.CharField(max_length=20,
                                    choices=[('lose_weight', 'Lose Weight'), ('maintain_weight', 'Maintain Weight'),
                                             ('build_muscle', 'Build Muscle')])

    def __str__(self):
        return self.name


