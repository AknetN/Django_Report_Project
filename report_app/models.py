from django.db import models

# Create your models here.
class Report(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('urgent', 'Urgent'),
        ('soon', 'Soon'),
    ]
    priority = models.CharField(max_length=255, choices=PRIORITY_CHOICES)
    completed = models.BooleanField(default=False)