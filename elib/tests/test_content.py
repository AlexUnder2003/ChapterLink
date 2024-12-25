from http import HTTPStatus

from tests.fixture import BaseTestCase


class HomepageListViewTestCase(BaseTestCase):
    """Тесты для главной страницы"""

    def test_homepage_list(self):
        books_created = self.create_books()
        response = self.client.get(self.home_page_url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        books_context = response.context["book_list"]
        self.assertEqual(len(books_context), 12)

        expected_titles = [book.title for book in books_created]
        actual_titles = [book.title for book in books_context]
        self.assertListEqual(actual_titles, expected_titles)


class FavouritesListViewTestCase(BaseTestCase):
    """Тесты для страницы избранных книг"""

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.expected_counts = ((cls.author_client, 1), (cls.reader_client, 0))

    def test_favourite_content(self):
        for user_client, count in self.expected_counts:
            with self.subTest(user_client=user_client):
                response = user_client.get(self.favourites_url)
                favorite_books = response.context["favorite_books"]
                self.assertEqual(len(favorite_books), count)
