# Generated by Django 2.1.3 on 2018-11-30 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0008_comment_comments_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comments_approved',
            field=models.BooleanField(default=False),
        ),
    ]