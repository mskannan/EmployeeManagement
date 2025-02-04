from django.db import models
from django.core.exceptions import ValidationError
import re

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)

    def clean(self):
        # Validate username length and alphanumeric characters
        if len(self.username) < 8 or not self.username.isalnum():
            raise ValidationError("Username must be alphanumeric and at least 8 characters long.")

        # Validate password strength (minimum 8 characters, 1 uppercase, 1 lowercase, 1 special char)
        password_regex = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[\W_]).{8,}$')
        if not password_regex.match(self.password):
            raise ValidationError("Password must be at least 8 characters long, contain 1 uppercase letter, 1 lowercase letter, and 1 special character.")

    def save(self, *args, **kwargs):
        self.clean()  # Trigger the custom validation
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
