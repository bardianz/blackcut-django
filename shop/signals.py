from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Product
import os

@receiver(pre_delete, sender=Product)
def delete_product_image(sender, instance, **kwargs):
    # Delete image file when product is deleted
    print("Deleting product image...")
    if instance.img:
        if os.path.isfile(instance.img.path):
            os.remove(instance.img.path)
            print("Image deleted successfully!")
        else:
            print("Image file does not exist.")
    else:
        print("No image associated with the product.")
