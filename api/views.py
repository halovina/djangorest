from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from borrower.models import Loan, Invoice
import json


# Create your views here.
def loan_list(request):
    loan = Loan.objects.all()
    data = {
        'resutl': list(loan.values('product_name','tenor'))
    }
    return JsonResponse(data)

def getInvoice(loanID):
    inv = Invoice.objects.filter(loan_id=loanID)
    data = []
    for x in inv:
        invlist = {}
        invlist['amount'] = x.amount
        invlist['invoice_date'] = str(x.invoice_date)
        data.append(invlist)
    return data

def loan_detail(request):
    loan = Loan.objects.all()
    data = []
    for x in loan:
        loanlist = {}
        loanlist['product_name'] = x.product_name
        loanlist['tenor']= x.tenor
        loanlist['detail_invoice'] = getInvoice(x.id)
        data.append(loanlist)
    
    return HttpResponse(json.dumps(data), content_type='application/json')