from django.conf import settings
from django.db import models


class Product(models.Model):
    """
    Model representing a product.

    Attributes:
        user (ForeignKey): Reference to the user who owns the product.
        name (str): The name of the product.
        barcode (str): The barcode of the product.
        price (Decimal): The price of the product.
        date_added (datetime): The date the product was added.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        help_text="The user who owns this product."
    )
    
    name = models.CharField(max_length=255)
    barcode = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
