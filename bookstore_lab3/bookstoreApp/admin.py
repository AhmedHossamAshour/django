from django.contrib import admin
from .models import Book,Author,ISBN,Publisher,Category,User

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(ISBN)
admin.site.register(Publisher)
admin.site.register(Category)
admin.site.register(User)
