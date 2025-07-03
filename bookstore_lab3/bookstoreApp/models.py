from django.db import models
from django.core.validators import MinLengthValidator

class User(models.Model):
    id= models.AutoField(primary_key=True,editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email=models.EmailField()
    username=models.CharField(max_length=100)
    
    
class Category(models.Model):
       id=models.AutoField(primary_key=True,editable=False)
       name=models.CharField(validators=[MinLengthValidator(2,"category needs at least 2 characters")])
       description=models.CharField(max_length=200)

        
    
class Author(models.Model):
    id= models.AutoField(primary_key=True,editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email=models.EmailField()

class Publisher(models.Model):
    id= models.AutoField(primary_key=True,editable=False)
    title=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
   

class Book(models.Model):
    title=models.CharField(validators=[MinLengthValidator(10,message="book title needs at least 10 characters")],max_length=50)
    content = models.TextField()
    published_at = models.DateTimeField()
    added_at=models.DateTimeField(auto_now_add=True)
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author,related_name='books')
    rate = models.DecimalField(max_digits=3, decimal_places=1,default=0.0)
    views = models.PositiveIntegerField(default=0)
    categories = models.ManyToManyField(Category,related_name='books')
    
class ISBN(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='isbn')
    code = models.CharField(max_length=13)

    def __str__(self):
        return f"{self.code} for {self.book.title}"