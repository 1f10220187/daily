# Generated by Django 4.2.7 on 2024-09-16 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('daily', '0007_alter_comment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='daily',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='daily.daily'),
        ),
    ]