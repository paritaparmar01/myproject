# Generated by Django 5.0.2 on 2024-03-09 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_loan_remarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
