from django.db import models
import uuid
from django.conf import settings


class Category(models.Model):
    id = models.UUIDField(primary_key=True,
                    default=uuid.uuid4,
                    editable=False
                          )
    name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='covers/')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Tags(models.Model):
    name = models.CharField(max_length=320)

class Articles(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    image = models.ImageField(upload_to='images/')
    publishing = models.BooleanField(default=False)