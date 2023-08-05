from django.db import models
from utils.models import CreateUpdate

# Create your models here.

class Loan(CreateUpdate):
    product_name = models.CharField(max_length=100)
    tenor = models.IntegerField(default=1)
    
class Invoice(CreateUpdate):
    loan = models.ForeignKey(
        Loan,
        related_name="loan_invoice",
        on_delete=models.CASCADE
    )
    amount = models.FloatField(default=0.0)
    invoice_date = models.DateField()
    
    class Meta:
        db_table = 'borrower_loan_invoice'

