from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet, InvoiceDetailViewSet

router = DefaultRouter()
router.register('invoices', InvoiceViewSet, basename='invoice')
router.register('invoice_details', InvoiceDetailViewSet, basename='invoicedetail')

urlpatterns = [
    path('', include(router.urls)),
]
