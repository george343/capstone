from django.contrib import admin
from .models import *


class VideoAdmin(admin.ModelAdmin):
    list_display = ["title", "url", "picture", "category", "user_upload"]


class CommentAdmin(admin.ModelAdmin):
    list_display = ["comment", "video", "commentor"]


admin.site.register(Video, VideoAdmin)
admin.site.register(Comment, CommentAdmin)
