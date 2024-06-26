# Generated by Django 5.0.2 on 2024-03-05 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_loan_rc_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='rc_book',
        ),
        migrations.AddField(
            model_name='loan',
            name='rc_book_radio',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3),
        ),
        migrations.AlterField(
            model_name='loan',
            name='document1',
            field=models.FileField(blank=True, null=True, upload_to='loan_documents/'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='loan',
            name='rc_book_image',
            field=models.ImageField(blank=True, null=True, upload_to='rc_book_images/'),
        ),
    ]
