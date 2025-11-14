from django.db import models
import datetime
class Posts(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.datetime.now)
    
    def __str__(self):
        return self.title
