# Generated by Django 5.1.4 on 2025-01-12 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0002_receipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipe',
            name='receipe_view_count',
            field=models.ImageField(default=1, upload_to=''),
        ),
    ]
