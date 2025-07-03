from django.shortcuts import render,redirect
from .models import Book,Author,Publisher
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def getBooks(req):
    books = Book.objects.all().prefetch_related("authors","publisher")
    authors=Author.objects.all()
    publishers=Publisher.objects.all()
    print(books[0].authors.all()[0].first_name)
    return render(req, 'bookstoreApp/books.html', {'books': books,'authors': authors,"publishers":publishers})

def AddBook(request):
        title= request.POST.get('title')
        content= request.POST.get('content')
        published_at= request.POST.get('published_at')
        authorID= request.POST.get('author')
        publisherID= request.POST.get('publisher')
        try:
            author = Author.objects.get(pk=authorID)
            publisher= Publisher.objects.get(pk=publisherID)
        except Author.DoesNotExist:
           return redirect('books_list')
        except Publisher.DoesNotExist:
            return redirect('books_list')
        
        book=Book.objects.create(
            title=title,
            content=content,
            published_at=published_at,
            publisher=publisher
        )
        book.authors.add(author)
        book.save()
        return redirect('books_list')
    
def EditBook(request):
    new_title = request.POST.get('title')
    new_content = request.Post.get("content")
    new_category=request.Post.get('category') or ''
        
    book = Book.objects.get(title=new_title)
    book.title = new_title
    book.content = new_content
    book.category = new_category
    book.save()
    
    return redirect('books_list')


def DeleteBook(request):
    title = request.POST.get('title')
    book = Book.objects.get(title=title)
    book.delete()
    return redirect('books_list')

@login_required
def Books(request):
    if request.method == 'POST':return AddBook(request)
    elif request.method == 'GET':return getBooks(request)
    elif request.method == 'PUT':return EditBook(request)
    elif request.method == 'PATCH':return EditBook(request)
    else: return DeleteBook(request)

@login_required
def getAllAuthors(req):
    
    if req.method == 'POST':
        first_name= req.POST.get('first_name')
        last_name= req.POST.get('last_name')
        email=req.POST.get('email')
        
        Author.objects.create(
                first_name=first_name,
                last_name =last_name,
                email=email
            )
        return redirect('author_list')
    authors = Author.objects.all()
    return render(req, 'bookstoreApp/authors.html',{'authors': authors})
            
     
    
    
    
@login_required
def getAllPublishers(req):
    if req.method == 'POST':
        title=req.POST.get('title')
        print(f"------------title----------{req.POST}-------")
        Publisher.objects.create(title=title)
        return redirect('publisher_list')
    
    publishers = Publisher.objects.all()
    return render(req, 'bookstoreApp/publishers.html',{'publishers': publishers})



def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('books_list')
    else:
        form = UserCreationForm()
    return render(request, 'bookstoreApp/signup.html', {'form': form})