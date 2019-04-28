from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc', 'updated_at', ]
    list_display_links = ['id', 'desc', ]
    list_filter = ['created_at', 'updated_at', ]
    search_fields = ['title', 'content', ]
