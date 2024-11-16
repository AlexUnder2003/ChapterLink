from django.views.generic import ListView
from books.models import Book


class HomepageListView(ListView):
    model = Book
    ordering = 'id'
    paginate_by = 12
