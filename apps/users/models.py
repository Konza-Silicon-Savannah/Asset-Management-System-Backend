from django.db import models
from uuid import uuid4
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    department = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    employeeNo = models.CharField(max_length=30, unique=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    bio = models.TextField()
    password = models.CharField(max_length=255, null=True)
    is_admin = models.BooleanField(default=False) # sudo user but doesnt have all the privileges in the system
    is_superuser = models.BooleanField(default=False) # super admin user with all sudo privileges
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'username', 'department', 'employeeNo']

    class Meta:
        db_table = "user"
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.id