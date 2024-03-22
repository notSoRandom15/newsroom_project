from django.contrib import admin
from .models import Category, Tags, Articles


admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Articles)