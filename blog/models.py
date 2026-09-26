from django.db import models
from mysite.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Post sarlavhasi"
    )
    image = models.ImageField(
        upload_to='posts/',
        verbose_name='Post Kontent'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    created_at = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.title} - {self.owner}"


