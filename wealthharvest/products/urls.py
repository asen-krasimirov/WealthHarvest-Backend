from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ExpenseViewSet, BarcodeScanView


router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('expenses', ExpenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('scan-barcode/', BarcodeScanView.as_view(), name='scan-barcode'),
]
