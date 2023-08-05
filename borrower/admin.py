from django.contrib import admin

# Register your models here.
from borrower.models import Loan, Invoice

admin.site.register(Loan)
admin.site.register(Invoice)