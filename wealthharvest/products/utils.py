from pyzbar.pyzbar import decode
from PIL import Image


def process_barcode(image_path):
    """
    Decode a barcode from an image file.

    Args:
        image_path (str): The path to the image containing the barcode.

    Returns:
        str: The decoded barcode data, or None if decoding fails.
    """

    image = Image.open(image_path)
    decoded = decode(image)
    if decoded:
        return decoded[0].data.decode('utf-8')
    return None
