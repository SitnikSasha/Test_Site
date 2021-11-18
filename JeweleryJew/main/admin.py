from django.contrib import admin
from .models import CategoryItem, Item
# Register your models here.


class CategoryItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('article', 'title', 'cat')


admin.site.register(CategoryItem, CategoryItemAdmin)
admin.site.register(Item, ItemAdmin)