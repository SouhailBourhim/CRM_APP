from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import timedelta
from django.utils import timezone

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    address = models.TextField()
    zip_code = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

class EmailVerificationToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def is_valid(self):
        expiry_time = self.created_at + timedelta(hours=24)
        return timezone.now() <= expiry_time and not self.is_verified

    def __str__(self):
        return f"{self.user.email} - {'Verified' if self.is_verified else 'Not Verified'}"