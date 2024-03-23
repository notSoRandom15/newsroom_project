from django.db import models
import uuid
from django.conf import settings
from ckeditor.fields import RichTextField


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
    description = RichTextField(blank=True, null=True)
    # description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    publishing = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    