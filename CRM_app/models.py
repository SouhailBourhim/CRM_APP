from django.db import models

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