from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid
from datetime import timedelta
from django.utils import timezone

# Create your models here.

MINUTES = timedelta(minutes=1)

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("email raqam majburiy.")
        if not username:
            raise ValueError("Foydalanuvchi nomi majburiy.")

        n_email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=n_email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(
            username=username,
            email=email,
            password=password,
            **extra_fields
        )

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    profile_image = models.ImageField(upload_to='users/', blank=True, null=True)
    name = models.CharField(max_length=50)
    bio = models.TextField(max_length=250, blank=True, null=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def str(self):
        return f"{self.username} - {self.email}"

class Email_OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    email = models.EmailField(unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    muddat = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.muddat:
            self.muddat = timezone.now() + MINUTES
        return super().save(*args, **kwargs)

    @property
    def muddati_otganmi(self):
        return timezone.now() >= self.muddat
    
    def __str__(self):
        return f"{self.user} - {self.code}"