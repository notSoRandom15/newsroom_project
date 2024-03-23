from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from .models import Menu, Block

@admin.register(Menu)
class MenuAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['name', "is_external", "is_active", "my_order"]

admin.site.register(Block)
