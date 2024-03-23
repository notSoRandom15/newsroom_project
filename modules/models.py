from django.db import models
from content.models import Category

class Menu(models.Model):
    name = models.CharField(max_length=250)
    link = models.URLField()
    is_external = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    my_order = models.PositiveBigIntegerField(default=0, blank=True, null=True)
    
    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return self.name

class Block(models.Model):
    BLOCK_CHOICES = [
        ('standard', 'Standard'),
        ('horizontal', 'Horizontal'),
        ('vertical', 'Vertical'),
    ]
    visual = models.CharField(max_length=10, choices=BLOCK_CHOICES)
    block_position = models.CharField(max_length=50)
    row = models.IntegerField()
    title = models.CharField(max_length=250)
    show_title = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    