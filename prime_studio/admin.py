
from django.contrib import admin
from .models import Gallery, Navigation, Painting, Terms


# Register your models here.
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    search_fields = ['title', 'id']
    list_display = ['title', 'id']
    ordering = ['id']


@admin.register(Navigation)
class NavigationAdmin(admin.ModelAdmin):
    search_fields = ['navigation_title', 'id']
    list_display = ['navigation_title', 'id']
    ordering = ['id']


@admin.register(Painting)
class PaintingAdmin(admin.ModelAdmin):
    search_fields = ['painting_level', 'id']
    list_display = ['painting_level', 'id']
    ordering = ['id']


@admin.register(Terms)
class TermsAdmin(admin.ModelAdmin):
    search_fields = ['terms_title', 'id']
    list_display = ['terms_title', 'id']
    ordering = ['id']
