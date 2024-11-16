from django.urls import path

from .views import search_books, BookDetailView

app_name = 'books'

urlpatterns = [
    path('', search_books, name='search_books'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
]
