from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, **fields):
        email = fields.pop('email', None)
        password = fields.get('password')

        if email is None:
            raise ValueError('Email field cannot be empty')

        email = self.normalize_email(email=email)
        user = self.model(email=email, **fields)
        user.set_password(raw_password=password)

        user.save(using=self._db)
        return user

    def create_user(self, **fields):
        fields.setdefault('is_superuser', False)
        fields.setdefault('is_staff', False)
        return self._create_user(**fields)

    def create_superuser(self, **fields):
        fields.setdefault('is_superuser', True)
        fields.setdefault('is_staff', True)
        return self._create_user(**fields)


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=300, null=True, blank=True)
    last_name = models.CharField(max_length=300, null=True, blank=True)
    nick_name = models.CharField(max_length=50, unique=True, null=True, blank=True)
    email = models.EmailField(max_length=300, unique=True, null=False, blank=False)
    date_joined = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.email}'
