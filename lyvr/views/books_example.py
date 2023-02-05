from django.shortcuts import render, get_object_or_404, redirect

from lyvr.forms import BookExampleForm
from lyvr.models import BookExample


def list(request):
    books = BookExample.objects.all()

    return render(request, 'books_example/book_list.html', {'books': books})


def create(request):
    if request.method == 'POST':
        form = BookExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-example-list')

    else:
        form = BookExampleForm()

    return render(request, 'books_example/book_form.html', {'form': form})


def detail(request, id):
    book = get_object_or_404(BookExample, pk=id)

    return render(request, 'books_example/book_detail.html', {'book': book})


def edit(request, id):
    book = get_object_or_404(BookExample, pk=id)

    if request.method == 'POST':
        form = BookExampleForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-example-list')

    else:
        form = BookExampleForm(instance=book)

    return render(request, 'books_example/book_form.html', {'form': form})


def delete(request, id):
    book = get_object_or_404(BookExample, pk=id)
    book.delete()
    
    return redirect('book-example-list')
