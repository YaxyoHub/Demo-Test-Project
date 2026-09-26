from django.db import models
from mysite.models import User

# Create your models here.

class Book(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=50
    )
    desc = models.TextField(
        max_length=150
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    count = models.IntegerField()
    is_avaible = models.BooleanField(
        default=True
    )
    created_at = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
