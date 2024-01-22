from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=50, **NULLABLE, verbose_name='Номер телефона')
    country = models.CharField(max_length=50, **NULLABLE, verbose_name='Страна')
    avatar = models.ImageField(upload_to='media/users/', **NULLABLE, verbose_name='Аватар')
    is_active = models.BooleanField(default=False, verbose_name='Статус активности')

    email_verificator = models.CharField(max_length=30, **NULLABLE, verbose_name='код верификации почты')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ('country', 'is_active')
