from django.urls import path

from .views import search_books, detailed_view

app_name = 'books'

urlpatterns = [
    path('', search_books, name='search_books'),
    path('<int:book_id>/', detailed_view, name='book_detail'),
]
