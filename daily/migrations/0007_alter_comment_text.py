# Generated by Django 5.1 on 2024-09-04 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily', '0006_comment_daily'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(default=None),
        ),
    ]