from django.db import models
from django.contrib.auth.models import AbstractUser



class Video(models.Model):
    title = models.CharField(max_length=128)
    video = models.FileField(upload_to='videos/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

class Worker(AbstractUser):
    title = models.CharField(max_length=100)  
    phone_number = models.CharField(max_length=15, blank=True, null=True)  
    is_active = models.BooleanField(default=True)  
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'
