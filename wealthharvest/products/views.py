from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import process_barcode


class BarcodeScanView(APIView):
    """
    API view to handle barcode scanning and decoding.

    Methods:
        post(request): Processes the uploaded image and decodes the barcode.
    """

    def post(self, request):
        """
        Handle POST request to decode a barcode from an uploaded image.

        Args:
            request (Request): The incoming HTTP request containing the image file.

        Returns:
            Response: Decoded barcode data or an error message.
        """
        
        image = request.FILES.get('image')
        barcode = process_barcode(image)
        if barcode:
            return Response({'barcode': barcode}, status=200)
        return Response({'error': 'Unable to decode barcode'}, status=400)
