from django.contrib import admin
from replitweblog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "file",
    ]
