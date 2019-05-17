from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    username = models.CharField(max_length=20, blank=False, null=False,
                                unique=True, db_index=True, primary_key=True)
    email = models.EmailField(blank=False, null=False, unique=True)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True,
                               verbose_name='Photo')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    def __str__(self):
        return self.username
