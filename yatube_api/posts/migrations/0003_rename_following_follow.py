# Generated by Django 5.1.6 on 2025-03-01 03:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_group_alter_comment_id_alter_post_id_following'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Following',
            new_name='Follow',
        ),
    ]
