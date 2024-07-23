import unittest
from src.main import cow_say


class TestMain(unittest.TestCase):
    def test_cow_say(self):
        self.assertEqual(cow_say(), "Moo! I'm a cow!")


if __name__ == "__main__":
    unittest.main()
