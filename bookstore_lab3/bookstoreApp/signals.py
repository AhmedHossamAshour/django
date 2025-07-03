from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book, ISBN
import random

@receiver(post_save, sender=Book)
def create_isbn_for_book(sender, instance, created, **kwargs):
    if created:
        fake_isbn = ''.join([str(random.randint(0, 9)) for _ in range(13)])
        ISBN.objects.create(book=instance, code=fake_isbn)