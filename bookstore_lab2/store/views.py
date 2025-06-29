from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import book

# Global data store
books = book.objects.all()
# next_id = 3  # To track next ID to assign


def book_list(request):
    return render(request, 'store/book_list.html', {'books': books})


def book_detail(request, book_id):
    bk = get_object_or_404(book, id=book_id)
    return render(request, 'store/book_detail.html', {'book': bk})


def book_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST.get('desc', '')
        rate = int(request.POST.get('rate', 5))
        genre = request.POST.get('genre', 'General')  # Not used in model unless added
        book.objects.create(title=title, desc=desc, rate=rate)
        return redirect('book_list')
    return render(request, 'store/book_form.html')


def book_edit(request, book_id):
    bk = get_object_or_404(book, id=book_id)
    if request.method == 'POST':
        bk.title = request.POST['title']
        bk.desc = request.POST['desc']
        bk.rate = int(request.POST['rate'])
        bk.save()
        return redirect('book_detail', book_id=book_id)
    return render(request, 'store/book_form.html', {'book': bk})


def book_delete(request, book_id):
    bk = get_object_or_404(book, id=book_id)
    if request.method == 'POST':
        bk.delete()
        return redirect('book_list')
    return render(request, 'store/book_confirm_delete.html', {'book': bk})
