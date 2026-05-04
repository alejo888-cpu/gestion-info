import unittest
from src.validate import validar_nombre

class TestValidate(unittest.TestCase):

    def test_nombre_valido(self):
        valido, _ = validar_nombre("Carlos")
        self.assertTrue(valido)

    def test_nombre_invalido(self):
        valido, _ = validar_nombre("")
        self.assertFalse(valido)

if __name__ == "__main__":
    unittest.main()