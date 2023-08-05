
from django.urls import path
from api import views

urlpatterns = [
    path('loan/list/', views.loan_list, name='loan-list'),
    path('loan/detail/', views.loan_detail, name='loan-detail')
    
]
