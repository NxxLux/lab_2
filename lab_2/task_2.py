BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})'


class Library:
    def __init__(self, books=None):
        # Если список книг не передан, инициализируем пустым списком
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        # Если в библиотеке нет книг, следующий ID будет 1
        if not self.books:
            return 1
        # Если книги есть, возвращаем ID следующей книги, увеличив последний ID на 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):
        # Ищем книгу с данным ID, если нет, возбуждаем исключение
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError(f"Книги с запрашиваемым id {book_id} не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
