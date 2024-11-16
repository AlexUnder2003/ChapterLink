from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import FavoriteBook, Book


@login_required
def add_favorite_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        created = FavoriteBook.objects.get_or_create(user=request.user,
                                                     book=book)

        if created:
            messages.success(request,
                             f"Книга '{book.title}' добавлена в ваши любимые!")
        else:
            messages.warning(request,
                             f"Книга '{book.title}' уже в списке любимых.")

    except Book.DoesNotExist:
        messages.error(request, "Книга не найдена.")

    return redirect('favourites:favourites')


def favourites_view(request):
    favorite_books = FavoriteBook.objects.filter(user=request.user).select_related('book')
    latest_book = favorite_books.last()
    other_books = favorite_books.exclude(id=latest_book.id) if latest_book else []

    return render(request, 'favourites/favourites.html', {
        'latest_book': latest_book,
        'other_books': other_books,
    })
