from django.db import models
from django.conf import settings

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.title
