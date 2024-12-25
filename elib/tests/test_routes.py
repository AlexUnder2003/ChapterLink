from http import HTTPStatus

from tests.fixture import BaseTestCase


class PublicAccessTests(BaseTestCase):
    """Тесты для маршутов, доступных всем пользоваетлям"""

    def test_pages_accessible(self):
        urls = (
            self.home_page_url,
            self.book_detail_url,
            self.login_url,
            self.signup_url,
        )
        for url in urls:
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, HTTPStatus.OK)


class AnonymousAccessTests(BaseTestCase):
    """Тесты для анонимного пользователя."""

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.protected_urls = (
            cls.favourites_url,
            cls.favourites_add,
        )

    def test_redirect_to_login(self):
        for url in self.protected_urls:
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertRedirects(response, self.login_url + f"?next={url}")


class AuthenticatedAccessTests(BaseTestCase):
    """Тесты для авторизованого пользователя."""

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.pages = (
            (cls.favourites_url, HTTPStatus.OK),
            (cls.favourites_add, HTTPStatus.FOUND),
        )

    def test_favourites_page(self):
        for url, status in self.pages:
            with self.subTest(url=url):
                response = self.author_client.get(url)
                self.assertEqual(response.status_code, status)
