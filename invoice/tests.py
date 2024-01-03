from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Invoice, InvoiceDetail
from django.urls import reverse

class InvoiceAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice_data = {'date': '2024-01-01', 'customer_name': 'Karunakar Balivada'}
        self.invoice = Invoice.objects.create(**self.invoice_data)
        self.invoice_detail_data = {
            'invoice': self.invoice, 
            'description': 'Product Purchase',
            'quantity': 2,
            'unitprice': 10.5,
            'price': 21.0
        }
        self.invoice_detail = InvoiceDetail.objects.create(**self.invoice_detail_data)


    def test_create_invoice(self):
        response = self.client.post('/api/invoices/', self.invoice_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 2)  

    def test_retrieve_invoice(self):
        response = self.client.get(f'/api/invoices/{self.invoice.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['date'], self.invoice_data['date'])
        self.assertEqual(response.data['customer_name'], self.invoice_data['customer_name'])

    def test_update_invoice(self):
        updated_data = {'customer_name': 'Karunakar Balivada', 'date': '2024-03-04'}
        response = self.client.put(reverse('invoice-detail', args=[self.invoice.id]), data=updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.invoice.refresh_from_db()
        self.assertEqual(str(self.invoice.date), updated_data['date'])
        self.assertEqual(self.invoice.customer_name, updated_data['customer_name'])

    def test_delete_invoice(self):
        response = self.client.delete(f'/api/invoices/{self.invoice.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Invoice.objects.count(), 0)

    def test_list_invoices(self):
        response = self.client.get('/api/invoices/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) 

class InvoiceDetailAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice_data = {'date': '2024-01-01', 'customer_name': 'Karunakar Balivada'}
        self.invoice = Invoice.objects.create(**self.invoice_data)
        self.invoice_detail_data = {
            'invoice': self.invoice,  
            'description': 'Purchase Product',
            'quantity': 2,
            'unitprice': 10.5,
            'price': 21.0
        }
        self.invoice_detail = InvoiceDetail.objects.create(**self.invoice_detail_data)

    def test_create_invoice_detail(self):
        invoice_id = self.invoice.id  
        self.invoice_detail_data['invoice'] = invoice_id 
        response = self.client.post(reverse('invoicedetail-list'), data=self.invoice_detail_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(InvoiceDetail.objects.count(), 2)

    def test_retrieve_invoice_detail(self):
        response = self.client.get(f'/api/invoice_details/{self.invoice_detail.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], self.invoice_detail_data['description'])
        self.assertEqual(response.data['quantity'], self.invoice_detail_data['quantity'])


    def test_update_invoice_detail(self):
        updated_data = {'description': 'newly purchased', 'quantity': 3, 'unitprice': 12.0, 'price': 36.0, 'invoice': self.invoice.id}
        response = self.client.put(reverse('invoicedetail-detail', args=[self.invoice_detail.id]), data=updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.invoice_detail.refresh_from_db()
        self.assertEqual(self.invoice_detail.description, updated_data['description'])
        self.assertEqual(self.invoice_detail.quantity, updated_data['quantity'])
        self.assertEqual(float(self.invoice_detail.unitprice), updated_data['unitprice'])
        self.assertEqual(float(self.invoice_detail.price), updated_data['price'])

    def test_delete_invoice_detail(self):
        response = self.client.delete(f'/api/invoice_details/{self.invoice_detail.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(InvoiceDetail.objects.count(), 0)

    def test_list_invoice_details(self):
        response = self.client.get('/api/invoice_details/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  
