from django.contrib import admin
from django.urls import path, include
from products.views import BarcodeScanView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('users.urls')),  # User registration routes
    path('api/', include('products.urls')),   # Products and barcode scanning
]
