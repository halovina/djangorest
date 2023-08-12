
from django.urls import path
# from api import views
from api import apiviews

urlpatterns = [
    # path('loan/list/', views.loan_list, name='loan-list'),
    # path('loan/detail/', views.loan_detail, name='loan-detail')
    path('loan/list/', apiviews.LoanList.as_view(), name='loan-list'),
    path('loan/list/<int:pk>', apiviews.LoanDetail.as_view(), name='loan-detail'),
    
]
