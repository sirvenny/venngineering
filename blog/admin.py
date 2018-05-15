from django.contrib import admin
from .models import Post
from django.db import models
from markdownx.widgets import AdminMarkdownxWidget
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.

# class PostAdmin(admin.ModelAdmin):
#     fields = ['author', 'title', 'text', 'created_date', 'published_date', 'tags']
#     formfield_overrides = {
#     models.TextField: {'widget': AdminMarkdownxWidget}
#     }
    # list_display = ('title', 'published_date')

admin.site.register(Post, MarkdownxModelAdmin)
# admin.site.register(Post, PostAdmin)
