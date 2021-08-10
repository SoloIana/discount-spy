from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=30)
    target_price = models.DecimalField(decimal_places=2, max_digits=10)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()
