from django.contrib import admin

from .models import Link


class LinkAdmin(admin.ModelAdmin):
    search_fields = ['title__icontains', 'description']
    list_display = ['title', 'user', 'domain', 'active']
    list_filter = ['user', 'active']
    date_hierarchy = 'created_on'


admin.site.register(Link, LinkAdmin)
