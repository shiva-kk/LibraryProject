import unittest
from library.library_item import LibraryItem

class TestLibraryItem(unittest.TestCase):
    def test_check_out(self):
        item = LibraryItem("Item 1", "Author 1", 1)
        self.assertEqual(item.check_out(), "Item 1 has been checked out.")
        self.assertEqual(item.check_out(), "Item 1 is already checked out.")

    def test_check_in(self):
        item = LibraryItem("Item 2", "Author 2", 2)
        self.assertEqual(item.check_in(), "Item 2 is already checked in.")
        item.check_out()
        self.assertEqual(item.check_in(), "Item 2 has been checked in.")

if __name__ == "__main__":
    unittest.main()
