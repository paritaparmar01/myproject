# Generated by Django 5.0.2 on 2024-03-10 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mo',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
