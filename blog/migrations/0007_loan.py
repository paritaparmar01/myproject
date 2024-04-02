# Generated by Django 5.0.2 on 2024-03-04 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('rc_book', models.CharField(max_length=10)),
                ('rc_book_image', models.ImageField(upload_to='rc_book_images/')),
                ('document1', models.FileField(upload_to='loan_documents/')),
                ('document2', models.FileField(blank=True, null=True, upload_to='loan_documents/')),
                ('document3', models.FileField(blank=True, null=True, upload_to='loan_documents/')),
                ('document4', models.FileField(blank=True, null=True, upload_to='loan_documents/')),
                ('document5', models.FileField(blank=True, null=True, upload_to='loan_documents/')),
            ],
        ),
    ]