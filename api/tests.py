# from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from borrower.models import Loan

class TestLoan(APITestCase):
    @staticmethod
    def sample_create_loan():
        return Loan.objects.create(
            product_name = "test produk pinjaman 1",
            tenor = 3
        )
    
    def test_loan_list(self):
        # '/api/loan'
        self.sample_create_loan()
        response =  self.client.get("/api/loan/", format='json')
        self.assertEqual(response.status_code, 200)
        jsd = response.json()
        self.assertEqual(len(jsd), 1)
        
    def test_create_loan(self):
        payload = {
            "product_name": "test create loan",
            "tenor": 35
        }
        response = self.client.post("/api/loan/", data=payload, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['tenor'], 35)
        
    def test_delete_data(self):
        
        payload = {
            "product_name": "test create loan",
            "tenor": 35
        }
        response1 = self.client.post("/api/loan/", data=payload, format='json')
        self.assertEqual(response1.status_code, 201)
        
        response2 = self.client.delete("/api/loan/{}".format(response1.json()['id']))
        self.assertEqual(response2.status_code, 204)
        
        
        

