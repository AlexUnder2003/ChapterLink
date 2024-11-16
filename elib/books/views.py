import typesense

from django.shortcuts import render, get_object_or_404

from .models import Book

client = typesense.Client({
    'nodes': [{
        'host': 'localhost',
        'port': '8108',
        'protocol': 'http'
    }],
    'api_key': 'xyz',
})


def search_books(request):
    title = request.GET.get('title')
    try:
        response = client.collections['books'].documents.search({
            'q': title,
            'query_by': 'title',
            'sort_by': 'sorting_id:asc'
        })

        book_ids = [hit['document']['sorting_id'] for hit in response['hits']]

        books = Book.objects.filter(id__in=book_ids)

        context = {'books': books}
        return render(request, 'books/books.html', context)

    except Exception as e:
        print(f"Ошибка поиска: {e}")
        return render(request, 'books/books.html', {'error': 'Произошла ошибка при поиске.'})



def detailed_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})

