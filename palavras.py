import argparse
import re
from collections import Counter

from stopwords import STOPWORDS


def contar(texto, ignorar=()):
    palavras = re.findall(r"\w+", texto.lower(), flags=re.UNICODE)
    palavras = [palavra for palavra in palavras if palavra not in ignorar]
    return dict(Counter(palavras))


def main():
    parser = argparse.ArgumentParser(description="Conta a frequência de palavras em um arquivo de texto.")
    parser.add_argument("arquivo", help="Caminho para o arquivo de texto")
    parser.add_argument("--top", type=int, default=5, help="Quantidade de palavras mais frequentes a exibir (padrão: 5)")
    parser.add_argument("--sem-stopwords", action="store_true", help="Ignora palavras comuns do português (artigos, preposições, etc.)")
    args = parser.parse_args()

    with open(args.arquivo, "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()

    ignorar = STOPWORDS if args.sem_stopwords else ()
    frequencias = contar(texto, ignorar=ignorar)
    mais_frequentes = Counter(frequencias).most_common(args.top)

    for palavra, quantidade in mais_frequentes:
        print(f"{palavra}: {quantidade}")


if __name__ == "__main__":
    main()
