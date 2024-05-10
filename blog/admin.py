from django.contrib import admin
from .models import Post, Category


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('title', 'published', 'author')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('name', 'created_at', 'updated_at')
