from django import forms
from .models import PolicyIssue, LoanEnquiry, InsuranceEnquiry,Loan,User

class PolicyIssueForm(forms.ModelForm):
    class Meta:
        model = PolicyIssue
        fields = '__all__'  # Corrected attribute value

class LoanEnquiryForm(forms.ModelForm):
    class Meta:
        model = LoanEnquiry
        fields = '__all__'  # Corrected attribute value

class InsuranceEnquiryForm(forms.ModelForm):
    class Meta:
        model = InsuranceEnquiry
        fields = ['name', 'number', 'email', 'vehicle_number', 'rc_book_radio', 'rc_book_image', 'previous_policy_radio', 'previous_policy_image', 'end_date']

from django import forms
from .models import LoanEnquiry

class LoanEnquiryForm(forms.ModelForm):
    class Meta:
        model = LoanEnquiry
        fields = ['name', 'number', 'email', 'rc_book_radio', 'rc_book_image', 'documents']

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = '__all__'  # or specify the fields you want to include in the form

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class DateForm(forms.Form):
    start = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    end = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))