from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=255 ,null=True)
    email = models.CharField(primary_key=True, max_length=59)
    password = models.CharField(max_length=42 ,null=True)

class User(models.Model):
    username = models.EmailField(primary_key=True)
    email= models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    mo = models.CharField(max_length=255 , default=None)
    def _str_(self):
        return self.username

class InsuranceEnquiry(models.Model):
    
    name = models.CharField(max_length=100, blank=True, null=True)
    number = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    vehicle_number = models.CharField(max_length=20, blank=True, null=True)
    rc_book_radio = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    rc_book_image = models.ImageField(upload_to='rc_book_images/', blank=True, null=True)
    previous_policy_radio = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    previous_policy_image = models.ImageField(upload_to='previous_policy_images/', blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

class LoanEnquiry(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    email = models.EmailField()
    rc_book_radio = models.CharField(max_length=10)
    rc_book_image = models.ImageField(upload_to='rc_book_images/')
    documents= models.ManyToManyField('Document')
    
    
    def __str__(self):
        return self.name

class Document(models.Model):
    document = models.FileField(upload_to='documents/')
    
    def __str__(self):
        return self.document.name
    
class PolicyIssue(models.Model):
    class Meta:
        ordering = ['date', 'name', 'number','ckyc', 'p_number', 'v_number', 'Vehicle', 'c_number', 'e_number', 'Location', 'HP_bank', 'business_type', 'insurance_type', 'insurance_portal', 'I_company', 'payment', 'payment_sos', 'PS_date', 'PE_date', 'Ncb', 'Premium', 'odNetPremium', 'commissionPercentage', 'payoutDiscount', 'PayoutAmount', 'profitResult', 'tdsPercentage', 'profitAfterTDSResult', 'netProfitResult', 'Executive', 'DSA']
    date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=25, blank=True, null=True)
    ckyc = models.CharField(max_length=255, blank=True, null=True)
    p_number = models.CharField(max_length=255, blank=True, null=True)
    v_number = models.CharField(max_length=255, blank=True, null=True)
    Vehicle = models.CharField(max_length=255, blank=True, null=True)
    c_number = models.CharField(max_length=255, blank=True, null=True)
    e_number = models.CharField(max_length=255, blank=True, null=True)
    Location = models.CharField(max_length=255, blank=True, null=True)
    HP_bank = models.CharField(max_length=255, blank=True, null=True)
    business_type = models.CharField(max_length=20, choices=[('New', 'New'), ('Data', 'Data'), ('Renewal', 'Renewal'), ('Endorsement', 'Endorsement')], default='Data')
    insurance_type = models.CharField(max_length=20, choices=[('Full', 'Full'), ('TP', 'TP'), ('SOD', 'SOD'), ('Package', 'Package'), ('Health', 'Health')], default='TP')
    insurance_portal = models.CharField(max_length=20, blank=True, null=True, choices=[('Mintpro', 'Mintpro'), ('Agency', 'Agency'), ('Ahmedabad', 'Ahmedabad'), ('IRSS', 'IRSS'), ('Probus', 'Probus'), ('Insurance_Dekho', 'Insurance_Dekho')], default='Agency')
    I_company = models.CharField(max_length=255, blank=True, null=True)
    payment = models.CharField(max_length=255, blank=True, null=True)
    payment_sos = models.CharField(max_length=255, blank=True, null=True)
    PS_date = models.DateField(blank=True, null=True)
    PE_date = models.DateField(blank=True, null=True)
    Ncb = models.IntegerField(blank=True, null=True)
    Premium = models.IntegerField(blank=True, null=True)
    odNetPremium = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    commissionPercentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    profitResult = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tdsPercentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    profitAfterTDSResult = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payoutDiscount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    PayoutAmount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    netProfitResult = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Executive = models.CharField(max_length=255, null=True)
    DSA = models.CharField(max_length=255, blank=True, null=True)

    def _str_(self):
        return f"{self.name}'s Policy Issue"


class Loan(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    email = models.EmailField()
    rc_book = models.BooleanField(default=False)  # Add rc_book field
    rc_book_image = models.ImageField(upload_to="rc_book_images/", blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)  # Update to TextField to store longer text
    document1 = models.FileField(upload_to="loan_documents/", blank=True, null=True)
    document2 = models.FileField(upload_to="loan_documents/", blank=True, null=True)
    document3 = models.FileField(upload_to="loan_documents/", blank=True, null=True)
    document4 = models.FileField(upload_to="loan_documents/", blank=True, null=True)
    document5 = models.FileField(upload_to="loan_documents/", blank=True, null=True)

    def __str__(self):
        return self.name




