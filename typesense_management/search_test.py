import typesense


client = typesense.Client({
    'nodes': [{
        'host': 'localhost',
        'port': '8108',
        'protocol': 'http'
    }],
    'api_key': 'xyz',
})

def search_book(title_or_author):
    try:
        response = client.collections['books'].documents.search({
            'q': title_or_author,
            'query_by': 'title, author',
            'sort_by': 'sorting_id:asc'
        })
        return response
    except Exception as e:
        print(f"Ошибка поиска: {e}")
        return None

result = search_book('Бе')
if result:
    for book in result['hits']:
        print(book['document'])
