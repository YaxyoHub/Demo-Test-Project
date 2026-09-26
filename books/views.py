from django.shortcuts import render
from .models import Book

# Create your views here.

def books_view(request):
    # books = Book.objects.all() -> hammasini olish
    # books = Book.objects.filter(is_avaible=True)
    # books = Book.objects.exclude(is_avaible=True)

    # __lt -> dan kam
    # __gt -> dan kup
    # books = Book.objects.filter(price__lt=24000)
    books = Book.objects.exclude(price__lt=24000)
    # books = Book.objects.filter(price__gt=24000)

    # __exact -> qiymati tochna bir xil bulgan
    # books = Book.objects.filter(title__exact="Python")

    return render(
        request,
        'books.html',
        context={
            'books': books
        }
    )
