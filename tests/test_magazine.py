import unittest
from library.magazine import Magazine

class TestMagazine(unittest.TestCase):
    def test_create_magazine(self):
        magazine = Magazine("Magazine 1", "Publisher 1", 1, 5)
        self.assertEqual(magazine.title, "Magazine 1")
        self.assertEqual(magazine.issue_number, 5)

if __name__ == "__main__":
    unittest.main()
