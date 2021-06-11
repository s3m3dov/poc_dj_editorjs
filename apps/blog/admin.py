from django.contrib import admin
from .models import (
    Article,
)

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = (
        "id",
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )
    list_filter = (
        "published",
        "publish_date",
    )
    
    search_fields = (
        "title",
        "subtitle",
        "slug",
        "body",
    )
    prepopulated_fields = {
        "slug": (
            "title",
            "subtitle",
        )
    }
    date_hierarchy = "publish_date"

"""
    list_editable = (
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )
"""