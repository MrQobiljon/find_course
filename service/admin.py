from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, WebService, Source


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category', 'web_service', 'get_url')
    list_display_links = ('name',)
    list_editable = ('category', 'web_service')

    def get_url(self, obj):
        return mark_safe(f'<a href="{obj.url}" target="_blank">Sahifaga o\'tish</a>')

    get_url.short_description = 'Link'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(WebService)
class WebServiceAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}