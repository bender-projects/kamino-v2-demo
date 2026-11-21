import unittest

from frases import contar_frases, media_palavras


class TestContarFrases(unittest.TestCase):
    def test_conta_frases_com_pontuacoes_variadas(self):
        resultado = contar_frases("Ola. Tudo bem? Sim!")
        self.assertEqual(resultado, 3)

    def test_texto_sem_pontuacao_final(self):
        resultado = contar_frases("Texto sem pontuacao final")
        self.assertEqual(resultado, 0)

    def test_texto_vazio(self):
        resultado = contar_frases("")
        self.assertEqual(resultado, 0)

    def test_pontuacao_repetida_conta_uma_frase(self):
        self.assertEqual(contar_frases("Que?! Espera... Ok."), 3)

    def test_pontuacao_solta_nao_conta_frase(self):
        self.assertEqual(contar_frases("Oi. !"), 1)


class TestMediaPalavras(unittest.TestCase):
    def test_media_palavras_basica(self):
        resultado = media_palavras("Eu vi o gato. O gato correu rapido.")
        self.assertEqual(resultado, 4.0)

    def test_media_palavras_com_pontuacoes_variadas(self):
        resultado = media_palavras("Isso e incrivel! Verdade? Sim.")
        self.assertAlmostEqual(resultado, 5 / 3)

    def test_media_palavras_texto_vazio(self):
        resultado = media_palavras("")
        self.assertEqual(resultado, 0)

    def test_media_palavras_sem_pontuacao_final(self):
        resultado = media_palavras("Texto sem pontuacao final")
        self.assertEqual(resultado, 0)


if __name__ == "__main__":
    unittest.main()
