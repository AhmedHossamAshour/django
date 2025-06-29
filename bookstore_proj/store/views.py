from django.shortcuts import render, redirect
from django.http import Http404

# Global data store
books = [
    {'id': 1, 'title': 'Book A', 'author': 'Author A', 'year': 2000, 'genre': 'Fiction'},
    {'id': 2, 'title': 'Book B', 'author': 'Author B', 'year': 2001, 'genre': 'Sci-Fi'},
]
next_id = 3  # To track next ID to assign


def book_list(request):
    return render(request, 'store/book_list.html', {'books': books})


def book_detail(request, book_id):
    for book in books:
        if book['id'] == book_id:
            return render(request, 'store/book_detail.html', {'book': book})
    raise Http404("Book not found")


def book_create(request):
    global next_id
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        year = int(request.POST['year'])
        genre = request.POST['genre']
        books.append({'id': next_id, 'title': title, 'author': author, 'year': year, 'genre': genre})
        next_id += 1
        return redirect('book_list')
    return render(request, 'store/book_form.html')


def book_edit(request, book_id):
    for book in books:
        if book['id'] == book_id:
            if request.method == 'POST':
                book['title'] = request.POST['title']
                book['author'] = request.POST['author']
                book['year'] = int(request.POST['year'])
                book['genre'] = request.POST['genre']
                return redirect('book_detail', book_id=book_id)
            return render(request, 'store/book_form.html', {'book': book})
    raise Http404("Book not found")


def book_delete(request, book_id):
    global books
    for book in books:
        if book['id'] == book_id:
            if request.method == 'POST':
                books = [b for b in books if b['id'] != book_id]
                return redirect('book_list')
            return render(request, 'store/book_confirm_delete.html', {'book': book})
    raise Http404("Book not found")
