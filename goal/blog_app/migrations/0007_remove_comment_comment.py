# Generated by Django 2.1.3 on 2018-11-29 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0006_auto_20181129_1151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment',
        ),
    ]
