from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    text = models.CharField(max_length=250, blank=True)
    create_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.title

    def get_author(self):
        return self.author

    def get_absolute_url(self):
        return reverse('blog_app:index')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comments_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    comments = models.CharField(max_length=250, blank=True)
    comments_approved = models.BooleanField(default=False)

    def approve(self):
        self.comments_approved = True
        self.save()

    def __str__(self):
        return self.comments

    def get_absolute_url(self):
        return reverse('blog_app:index')
