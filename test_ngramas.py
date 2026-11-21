import unittest

from ngramas import mais_frequentes


class TestMaisFrequentes(unittest.TestCase):
    def test_bigrama_padrao(self):
        resultado = mais_frequentes("o gato e o cachorro e o gato e o passaro")
        self.assertEqual(resultado[0], ("e o", 3))

    def test_maiusculas_sao_ignoradas(self):
        resultado = mais_frequentes("Casa Bonita aqui, CASA BONITA aqui, casa bonita")
        self.assertEqual(resultado[0], ("casa bonita", 3))

    def test_pontuacao_e_ignorada(self):
        resultado = mais_frequentes("Ola, mundo! Tudo bem? Ola; mundo.")
        self.assertEqual(resultado[0], ("ola mundo", 2))

    def test_texto_vazio(self):
        resultado = mais_frequentes("")
        self.assertEqual(resultado, [])

    def test_tamanho_trigrama(self):
        resultado = mais_frequentes("o rato roeu a roupa o rato roeu a roupa", tamanho=3)
        self.assertEqual(resultado[0], ("o rato roeu", 2))

    def test_tamanho_maior_que_texto(self):
        resultado = mais_frequentes("uma frase curta", tamanho=5)
        self.assertEqual(resultado, [])

    def test_top_limita_quantidade(self):
        resultado = mais_frequentes("maca maca banana banana banana uva uva pera", tamanho=1, top=2)
        self.assertEqual(resultado, [("banana", 3), ("maca", 2)])


if __name__ == "__main__":
    unittest.main()
