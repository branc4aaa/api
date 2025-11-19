from django.db import models
import datetime
class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(default=datetime.datetime.now)
    author = models.CharField(max_length=50, default='Anonymous')
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    def __str__(self):
        return self.title
