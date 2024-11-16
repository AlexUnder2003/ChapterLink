import typesense


class Manager:
    def __init__(self) -> None:
        self.client = typesense.Client({
            'nodes': [{
                'host': 'localhost',
                'port': '8108',
                'protocol': 'http'
            }],
            'api_key': 'xyz',
            'connection_timeout_seconds': 2
        })

    def create_collection(self, schema) -> None:
        try:
            self.client.collections.create(schema)
            print("Коллекция успешно создана.")
        except Exception as e:
            print(f"Коллекция уже существует или ошибка: {e}")

    def get_collections(self):
        try:
            collections = self.client.collections.retrieve()
            print(collections)
        except Exception as e:
            print(f"Ошибка при получении коллекций: {e}")

    def delete_collection(self, name) -> None:
        self.client.collections[name].delete()


schema = ({
    'name': 'books',
    'fields': [
        {'name': 'sorting_id', 'type': 'int32', 'optional': False, 'index': True, 'store': True},
        {'name': 'title', 'type': 'string', 'optional': False, 'index': True, 'store': True},
        {'name': 'author', 'type': 'string', 'optional': False, 'index': True, 'store': True}
    ],
    'default_sorting_field': 'sorting_id'
})

manage = Manager()

manage.create_collection(schema)
