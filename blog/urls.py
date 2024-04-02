# blog/urls.py
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('', home, name='home'),
    # path('register/', register, name='register'),
    # path('login/', login, name='login'),
    path('forgotpwd/', forgot_password, name='forgot_password'),
    # path('register/', register, name="register"),
    # path('login/', login_view, name="login"),
    # path('forgotpwd/', forgotPwd, name="forgotpwd"),
    path('success/', success, name='success'),
    path('form/',insurance_enquiry, name='insurance_enquiry'),
    path('update_record/<int:record_id>/',update_record, name='update_record'),
    path('edit_form/<int:record_id>/',edit_view, name='edit_view'),
    path('form/<int:record_id>/',insurance_enquiry, name='insurance_enquiry'),
    path('insurance_enquiry/<int:record_id>/',insurance_enquiry, name='insurance_enquiry'),
    path('loan/', loan, name='loan'),
    path('policyissue/', policy_issue, name="policy_issue"),
    path('uploadxlspolicyissue/', upload_policy, name="upload_policy"),
    path('delete_enquiry/<int:enquiry_id>/', delete_enquiry, name='delete_enquiry'),
    path('policyissue/<int:record_id>/delete/', delete_record, name='delete_record'),
    path('delete_loan_record/<int:record_id>/', delete_loan_record, name='delete_loan_record'),
    path('get_record/<int:record_id>/', get_record, name='get_record'),
    # path('update_record/<int:record_id>/', update_record, name='update_record'),
    path('get_record/<int:record_id>/', get_record, name='get_record'),
    path('update_record/<int:record_id>/', update_record, name='update_record'),
    path('update_policy/<int:record_id>/',update_policy, name='update_policy'),
    path('edit_loan/<int:record_id>/', edit_loan, name='edit_loan'),
    path('update_loan/<int:record_id>/', update_loan, name='update_loan'),
    path('edit_policy/<int:record_id>/', edit_policy, name='edit_policy'),
    path('update_enquiry/<int:record_id>/', update_insurance_enquiry, name='update_enquiry'),
    path('download/', download_data, name='download_data'),
    path('renewal/',renewal,name='renewal'),
    path('get_data/', get_data, name='get_data'),
    path('',SignupPage,name='signup'),
    path('login/',LoginPage,name='login'),
    path('home/',HomePage,name='home'),
    # path('chart/',chart,name='chart'),
    path('enquiry2/',enquiry2,name='enquiry2'),
    path('fetch-data/', fetch_data, name='fetch-data'),
    path('logout/', Logout, name='logout'),
    path('loan_dashboard/', loan_dashboard, name='loan_dashboard'),  
    path('insurance_dashboard/', insurance_dashboard, name='insurance_dashboard'), 
    path('untitle/', untitle, name='untitle'),   
    path('edit_form/<int:pk>/', edit_view, name='edit_form'),
    path('edit_form/<int:record_id>/', edit_view, name='edit_form'),
    
    


]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
