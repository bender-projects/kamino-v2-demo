import re


def contar_frases(texto):
    return len(re.findall(r"[^.!?]*[.!?]", texto))


def media_palavras(texto):
    total_frases = contar_frases(texto)
    if total_frases == 0:
        return 0
    total_palavras = len(re.findall(r"\w+", texto, flags=re.UNICODE))
    return total_palavras / total_frases
