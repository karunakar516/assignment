from rest_framework import serializers
from .models import Invoice, InvoiceDetail
class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = '__all__'

class InvoiceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['date', 'customer_name']
        extra_kwargs = {'date': {'required': False}, 'customer_name': {'required': False}}



class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(required=False,many=True, read_only=True)
    class Meta:
        model = Invoice
        fields = '__all__'

class InvoiceDetailUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = ['description', 'quantity', 'unitprice', 'price']
        extra_kwargs = {'unitprice': {'required': False}, 'price': {'required': False},'quantity':{'required':False},'description':{'required':False}}
