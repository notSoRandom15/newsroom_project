from django.db import models
import uuid


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
    