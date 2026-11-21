import json
import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import NamedTemporaryFile

from palavras import contar
from stopwords import STOPWORDS


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

    def test_ignorar_remove_palavras_informadas(self):
        resultado = contar("o gato e o cachorro", ignorar={"o", "e"})
        self.assertEqual(resultado, {"gato": 1, "cachorro": 1})

    def test_ignorar_com_stopwords(self):
        resultado = contar("o rato roeu a roupa do rei de roma", ignorar=STOPWORDS)
        self.assertEqual(resultado, {"rato": 1, "roeu": 1, "roupa": 1, "rei": 1, "roma": 1})

    def test_min_letras_remove_palavras_curtas(self):
        resultado = contar("eu vi um gato e um cachorro", min_letras=4)
        self.assertEqual(resultado, {"gato": 1, "cachorro": 1})


class TestMain(unittest.TestCase):
    def executar(self, *args):
        return subprocess.run(
            [sys.executable, "palavras.py", *args],
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent,
        )

    def test_opcao_top(self):
        with NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as arquivo:
            arquivo.write("maca maca banana banana banana uva uva pera")
            caminho = arquivo.name

        resultado = self.executar(caminho, "--top", "2")
        linhas = resultado.stdout.strip().splitlines()

        self.assertEqual(len(linhas), 2)
        self.assertEqual(linhas[0], "banana: 3")
        self.assertEqual(linhas[1], "maca: 2")

    def test_opcao_sem_stopwords(self):
        with NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as arquivo:
            arquivo.write("o gato e o cachorro e o passaro")
            caminho = arquivo.name

        resultado = self.executar(caminho, "--sem-stopwords", "--top", "3")
        linhas = resultado.stdout.strip().splitlines()

        self.assertIn("gato: 1", linhas)
        self.assertIn("cachorro: 1", linhas)
        self.assertIn("passaro: 1", linhas)
        self.assertFalse(any(linha.startswith("o:") for linha in linhas))
        self.assertFalse(any(linha.startswith("e:") for linha in linhas))

    def test_opcao_formato_json(self):
        with NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as arquivo:
            arquivo.write("maca maca banana banana banana uva uva pera")
            caminho = arquivo.name

        resultado = self.executar(caminho, "--top", "2", "--formato", "json")
        dados = json.loads(resultado.stdout)

        self.assertEqual(dados, [{"palavra": "banana", "contagem": 3}, {"palavra": "maca", "contagem": 2}])

    def test_opcao_min_letras(self):
        with NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as arquivo:
            arquivo.write("eu vi um gato e um cachorro")
            caminho = arquivo.name

        resultado = self.executar(caminho, "--min-letras", "4", "--top", "10")
        linhas = resultado.stdout.strip().splitlines()

        self.assertIn("gato: 1", linhas)
        self.assertIn("cachorro: 1", linhas)
        self.assertFalse(any(linha.startswith("eu:") for linha in linhas))
        self.assertFalse(any(linha.startswith("vi:") for linha in linhas))
        self.assertFalse(any(linha.startswith("um:") for linha in linhas))


if __name__ == "__main__":
    unittest.main()
