# Generated by Django 3.2 on 2023-07-30 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactblog', '0006_auto_20230729_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='description',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='question',
        ),
    ]
