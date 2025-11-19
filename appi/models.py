from django.db import models
from django.contrib.auth.models import User
import datetime
class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(default=datetime.datetime.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    def __str__(self):
        return self.title
