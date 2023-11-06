import unittest
from library.book import Book

class TestBook(unittest.TestCase):
    def test_create_book(self):
        book = Book("Book 1", "Author 1", 1, 200)
        self.assertEqual(book.title, "Book 1")
        self.assertEqual(book.page_count, 200)

if __name__ == "__main__":
    unittest.main()
