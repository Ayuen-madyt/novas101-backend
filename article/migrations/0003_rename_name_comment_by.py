# Generated by Django 3.2 on 2021-04-26 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_rename_view_views_views'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='by',
        ),
    ]
