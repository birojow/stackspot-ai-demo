import unittest

def soma(x, y):
    return x + y

class TestSoma(unittest.TestCase):
    def test_soma_numeros_positivos(self):
        self.assertEqual(soma(3, 4), 7)

    def test_soma_numeros_negativos(self):
        self.assertEqual(soma(-1, -1), -2)

    def test_soma_numeros_positivo_negativo(self):
        self.assertEqual(soma(-5, 5), 0)

if __name__ == '__main__':
    unittest.main()
