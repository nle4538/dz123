from django.shortcuts import render, redirect
from .models import Reader, Book
from .forms import ReaderForm, BookForm

def add_reader(request):
    if request.method == "POST":
        form = ReaderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reader_list')
    else:
        form = ReaderForm()
    return render(request, 'add_reader.html', {'form': form})

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})
def edit_reader(request, reader_id):
    reader = get_object_or_404(Reader, id=reader_id)
    if request.method == "POST":
        form = ReaderForm(request.POST, instance=reader)
        if form.is_valid():
            form.save()
            return redirect('reader_list')
    else:
        form = ReaderForm(instance=reader)
    return render(request, 'edit_reader.html', {'form': form})

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})
def delete_reader(request, reader_id):
    reader = get_object_or_404(Reader, id=reader_id)
    if request.method == "POST":
        reader.delete()
        return redirect('reader_list')
    return render(request, 'confirm_delete.html', {'object': reader})

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'confirm_delete.html', {'object': book})

