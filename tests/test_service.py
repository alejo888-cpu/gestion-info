import unittest
from src.service import new_register, search_record

class TestService(unittest.TestCase):

    def test_new_register(self):
        result = new_register("100", "Test")
        self.assertIn("correctamente", result)

    def test_search_record(self):
        new_register("101", "Juan")
        result = search_record("101")
        self.assertEqual(result["nombre"], "Juan")

if __name__ == "__main__":
    unittest.main()