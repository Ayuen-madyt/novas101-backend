# Generated by Django 3.2.4 on 2021-06-25 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_alter_article_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('NEWS', 'NEWS'), ('SPORTS', 'SPORTS'), ('LIFESTYLE', 'LIFESTYLE'), ('FASHION', 'FASHION'), ('ENTERTAINMENT', 'ENTERTAINMENT'), ('BUSINESS', 'BUSINESS'), ('TECHNOLOGY', 'TECHONOLOGY')], max_length=150),
        ),
    ]
