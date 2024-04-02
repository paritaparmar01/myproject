# Generated by Django 5.0.2 on 2024-02-28 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_loanenquiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='PolicyIssue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('number', models.CharField(blank=True, max_length=25, null=True)),
                ('p_number', models.CharField(blank=True, max_length=255, null=True)),
                ('v_number', models.CharField(blank=True, max_length=255, null=True)),
                ('Vehicle', models.CharField(blank=True, max_length=255, null=True)),
                ('c_number', models.CharField(blank=True, max_length=255, null=True)),
                ('e_number', models.CharField(blank=True, max_length=255, null=True)),
                ('Location', models.CharField(blank=True, max_length=255, null=True)),
                ('HP_bank', models.CharField(blank=True, max_length=255, null=True)),
                ('business_type', models.CharField(choices=[('New', 'New'), ('Data', 'Data'), ('Renewal', 'Renewal'), ('Endorsement', 'Endorsement')], default='Data', max_length=20)),
                ('insurance_type', models.CharField(choices=[('Full', 'Full'), ('TP', 'TP'), ('SOD', 'SOD'), ('Package', 'Package'), ('Health', 'Health')], default='TP', max_length=20)),
                ('insurance_portal', models.CharField(blank=True, choices=[('Mintpro', 'Mintpro'), ('Agency', 'Agency'), ('Ahmedabad', 'Ahmedabad'), ('IRSS', 'IRSS'), ('Probus', 'Probus'), ('Insurance_Dekho', 'Insurance_Dekho')], default='Agency', max_length=20, null=True)),
                ('I_company', models.CharField(blank=True, max_length=255, null=True)),
                ('payment', models.CharField(blank=True, max_length=255, null=True)),
                ('payment_sos', models.CharField(blank=True, max_length=255, null=True)),
                ('PS_date', models.DateField(blank=True, null=True)),
                ('PE_date', models.DateField(blank=True, null=True)),
                ('Ncb', models.IntegerField(blank=True, null=True)),
                ('Premium', models.IntegerField(blank=True, null=True)),
                ('odNetPremium', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('commissionPercentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('profitResult', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('tdsPercentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('profitAfterTDSResult', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('payoutDiscount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('PayoutAmount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('netProfitResult', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Executive', models.CharField(max_length=255, null=True)),
                ('DSA', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['date', 'name', 'number', 'p_number', 'v_number', 'Vehicle', 'c_number', 'e_number', 'Location', 'HP_bank', 'business_type', 'insurance_type', 'insurance_portal', 'I_company', 'payment', 'payment_sos', 'PS_date', 'PE_date', 'Ncb', 'Premium', 'odNetPremium', 'commissionPercentage', 'payoutDiscount', 'PayoutAmount', 'profitResult', 'tdsPercentage', 'profitAfterTDSResult', 'netProfitResult', 'Executive', 'DSA'],
            },
        ),
    ]
