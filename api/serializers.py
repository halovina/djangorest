from borrower.models import Loan, Invoice
from rest_framework import serializers

class InvoiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields= ['id','amount','invoice_date']

class LoanSerializers(serializers.ModelSerializer):
    loan_invoice = InvoiceSerializers(many=True)
    class Meta:
        model = Loan
        fields = ['id','product_name','tenor','loan_invoice']
        
class CRUDLoanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ['id','product_name','tenor']