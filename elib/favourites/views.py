from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView

from .models import FavoriteBook, Book


@login_required
def add_favorite_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        created = FavoriteBook.objects.get_or_create(
            user=request.user, book=book
        )
        if created:
            messages.success(
                request, f"Книга '{book.title}' добавлена в ваши любимые!"
            )
        else:
            messages.warning(
                request, f"Книга '{book.title}' уже в списке любимых."
            )
    except Book.DoesNotExist:
        messages.error(request, "Книга не найдена.")

    return redirect("favourites:favourites")


class FavouritesView(LoginRequiredMixin, ListView):
    model = FavoriteBook
    template_name = "favourites/favourites.html"
    context_object_name = "favorite_books"

    def get_queryset(self):
        # Основная выборка книг пользователя
        return FavoriteBook.objects.filter(
            user=self.request.user
        ).select_related("book")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        favorite_books = context["favorite_books"]

        # Последняя книга
        latest_book = favorite_books.last()
        context["latest_book"] = latest_book

        # Другие книги
        context["other_books"] = (
            favorite_books.exclude(id=latest_book.id) if latest_book else []
        )
        return context
