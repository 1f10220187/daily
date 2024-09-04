from django.db import models

import datetime
# Create your models here.

class Daily(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    daily = models.ForeignKey(Daily, on_delete=models.CASCADE)
    text=models.TextField(default=None)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text