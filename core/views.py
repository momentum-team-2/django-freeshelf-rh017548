from django.shortcuts import render, redirect, get_object_or_404
from .models import Books
from .forms import BookForm
from django.contrib.auth.decorators import login_required

# Create your views here.



def list_books(request):
    books = Books.objects.all().order_by('-id')
    return render(request, "core_temp/list_books.html",
                  {"books": books})


def home(request):
    if request.user.is_authenticated:
        return redirect('list_books')
    return render(request, 'core_temp/home.html')


def show_book(request, pk):
    book = get_object_or_404(Books, pk=pk)
    form = BookForm()
    return render(request, "core_temp/show_book.html", {"book": book, "pk": pk, "form": form})


def add_book(request):
    if request.method == 'GET':
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_books')

    return render(request, "core_temp/add_book.html", {"form": form})


def edit_book(request, pk):
    book = get_object_or_404(Books, pk=pk)
    if request.method == 'GET':
        form = BookForm(instance=book)
    else:
        form = BookForm(data=request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(to='list_books')

    return render(request, "core_temp/edit_book.html", {
        "form": form,
        "book": book
    })


def delete_book(request, pk):
    book = get_object_or_404(Books, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect(to='list_books')

    return render(request, "core_temp/delete_book.html",
                  {"book": book})