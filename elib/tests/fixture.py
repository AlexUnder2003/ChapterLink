from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from books.models import Book
from favourites.models import FavoriteBook

User = get_user_model()


class BaseTestCase(TestCase):
    """Базовый класс для тестов."""

    @classmethod
    def setUpTestData(cls):
        cls.reader_user = User.objects.create_user(username="reader_user")
        cls.author_user = User.objects.create_user(username="author_user")

        cls.reader_client = Client()
        cls.reader_client.force_login(cls.reader_user)

        cls.author_client = Client()
        cls.author_client.force_login(cls.author_user)

        cls.book = Book.objects.create(
            title="Пример книги",
            author="Автор Примера",
            description="Краткое описание книги.",
            full_description="Полное описание книги, больше информации.",
            published_date="2024-01-01",
            image="",
        )

        cls.favourite_book = FavoriteBook.objects.create(
            user=cls.author_user, book=cls.book
        )

        cls.home_page_url = reverse("homepage:home")
        cls.favourites_url = reverse("favourites:favourites")
        cls.favourites_add = reverse("favourites:add_favorite_book", args=[1])
        cls.book_detail_url = reverse("books:book_detail", args=[1])
        cls.login_url = reverse("login")
        cls.signup_url = reverse("registration")
        cls.search_url = reverse("books:search_books")

    @classmethod
    def create_books(cls, count=12):
        """Метод для создания книг и очистки базы."""
        Book.objects.all().delete()
        books = [
            Book(
                title=f"Пример книги {i}",
                author=f"Автор {i}",
                description=f"Краткое описание книги {i}.",
                full_description=f"Полное описание книги {i}",
                published_date="2024-01-01",
                image="",
            )
            for i in range(1, count + 1)
        ]
        Book.objects.bulk_create(books)
        return books
