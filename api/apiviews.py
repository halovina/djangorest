from borrower.models import Loan
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .serializers import LoanSerializers

class LoanList(APIView):
    def get(self, request):
        loan = Loan.objects.all()
        data = LoanSerializers(loan, many=True).data
        return Response(data)
    
    
class LoanDetail(APIView):
    def get(self, request, pk):
        loan = get_object_or_404(Loan, pk=pk)
        data = LoanSerializers(loan).data
        return Response(data)