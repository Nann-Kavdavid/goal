from django.forms import ModelForm
from blog_app.models import Post, Comment
from django import forms


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'create_date']
        labels = {
            'title': 'Goal',
            'text': 'Short description',
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comments', 'comments_approved']





