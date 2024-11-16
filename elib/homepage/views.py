from django.shortcuts import render
from books.models import Book


def homepage(request):
    books_rev = Book.objects.all().order_by('-id')
    context = {'books': books_rev}
    return render(request, 'homepage/homepage.html', context)
