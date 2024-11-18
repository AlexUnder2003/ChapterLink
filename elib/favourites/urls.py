from django.urls import path
from .views import FavouritesView, add_favorite_book

app_name = 'favourites'

urlpatterns = [
    path('', FavouritesView.as_view(), name='favourites'),
    path('add/<int:book_id>/', add_favorite_book, name='add_favorite_book'),
]