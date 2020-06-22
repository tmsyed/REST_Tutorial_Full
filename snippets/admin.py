from django.contrib import admin
from .models import Snippet


class SnippetAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'language', 'style', 'owner']
    list_filter = ['created']
    search_fields = ['title', 'language']


admin.site.register(Snippet, SnippetAdmin)