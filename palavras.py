import re
import sys
from collections import Counter


def contar(texto):
    palavras = re.findall(r"\w+", texto.lower(), flags=re.UNICODE)
    return dict(Counter(palavras))


def main():
    if len(sys.argv) < 2:
        print("Uso: python3 palavras.py <arquivo>")
        sys.exit(1)

    caminho = sys.argv[1]
    with open(caminho, "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()

    frequencias = contar(texto)
    mais_frequentes = Counter(frequencias).most_common(5)

    for palavra, quantidade in mais_frequentes:
        print(f"{palavra}: {quantidade}")


if __name__ == "__main__":
    main()
