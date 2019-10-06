from django.contrib import admin
from blog_app.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'title', 'text', 'create_date',)
    fields = ('author', 'title', 'text', 'create_date')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'pk', 'post', 'comments', 'comments_by', 'comments_approved')
