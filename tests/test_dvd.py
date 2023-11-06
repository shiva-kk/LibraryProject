import unittest
from library.dvd import DVD

class TestDVD(unittest.TestCase):
    def test_create_dvd(self):
        dvd = DVD("DVD 1", "Director 1", 1, 120)
        self.assertEqual(dvd.title, "DVD 1")
        self.assertEqual(dvd.run_time, 120)

if __name__ == "__main__":
    unittest.main()
