import re
from collections import Counter


def mais_frequentes(texto, tamanho=2, top=5):
    palavras = re.findall(r"\w+", texto.lower(), flags=re.UNICODE)
    ngramas = [" ".join(palavras[i:i + tamanho]) for i in range(len(palavras) - tamanho + 1)]
    return Counter(ngramas).most_common(top)
