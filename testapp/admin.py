from django.contrib import admin
from .models import Blog
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        ('title',               {'fields': ['title']}),
        ('content information', {'fields': ['content', 'author']}),
        ('images',              {'fields': ['image']}),
        ('like',              {'fields': ['likes']}),
    ]
    list_display = ['title', 'date']
    search_fields = ['title', 'content']

admin.site.register(Blog, BlogAdmin)