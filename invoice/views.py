from rest_framework import viewsets
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer,InvoiceUpdateSerializer,InvoiceDetailUpdateSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    def get_serializer_class(self):
        if self.action == 'update':
            return InvoiceUpdateSerializer
        return InvoiceSerializer

class InvoiceDetailViewSet(viewsets.ModelViewSet):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer
    def get_serializer_class(self):
        if self.action == 'update':
            return InvoiceDetailUpdateSerializer
        return InvoiceSerializer
