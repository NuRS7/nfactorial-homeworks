class BooksRepository:
    def __init__(self):
        self.books = [
            {
                "id": 1,
                "title": "To Kill a Mockingbird",
                "author": "Harper Lee",
                "year": 1960,
                "total_pages": 336,
                "genre": "Fiction",
            },
            {
                "id": 2,
                "title": "1984",
                "author": "George Orwell",
                "year": 1949,
                "total_pages": 328,
                "genre": "Dystopian",
            },
            {
                "id": 3,
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "year": 1925,
                "total_pages": 180,
                "genre": "Classic",
            },
            {
                "id": 4,
                "title": "The Lord of the Rings",
                "author": "J.R.R. Tolkien",
                "year": 1954,
                "total_pages": 1178,
                "genre": "Fantasy",
            },
            {
                "id": 5,
                "title": "The Catcher in the Rye",
                "author": "J.D. Salinger",
                "year": 1951,
                "total_pages": 224,
                "genre": "Coming-of-age",
            },
        ]

    def get_all(self):
        return self.books

    def get_one(self, id):
        try:
            id = int(id)
        except ValueError:
            return None

        for book in self.books:
            if book["id"] == id:
                return book
        return None

    def save(self, book):
        if not isinstance(book, dict):
            raise ValueError("Book must be a dictionary")

        required_keys = ["title", "author", "year", "total_pages", "genre"]
        if not all(key in book for key in required_keys):
            raise ValueError("Book must have all required keys")

        book["id"] = max(b["id"] for b in self.books) + 1 if self.books else 1
        self.books.append(book)
        return book