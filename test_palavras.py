import unittest

from palavras import contar


class TestContar(unittest.TestCase):
    def test_maiusculas_sao_ignoradas(self):
        resultado = contar("Casa casa CASA")
        self.assertEqual(resultado, {"casa": 3})

    def test_pontuacao_e_ignorada(self):
        resultado = contar("Ola, mundo! Ola; mundo.")
        self.assertEqual(resultado, {"ola": 2, "mundo": 2})

    def test_texto_vazio(self):
        resultado = contar("")
        self.assertEqual(resultado, {})


if __name__ == "__main__":
    unittest.main()
