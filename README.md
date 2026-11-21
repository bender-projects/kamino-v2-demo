# kamino-v2-demo

Contador de palavras: conta a frequência de cada palavra em um texto, sem
diferenciar maiúsculas de minúsculas e ignorando pontuação.

## Como rodar o programa

```bash
python3 palavras.py caminho/para/arquivo.txt
```

O programa imprime as 5 palavras mais frequentes do arquivo, com suas
respectivas contagens.

## Opções

- `--top N`: define quantas palavras mais frequentes exibir (padrão: 5).
- `--sem-stopwords`: ignora palavras comuns do português (artigos,
  preposições, conjunções e pronomes), definidas em `stopwords.py`.

### Exemplo

```bash
python3 palavras.py texto.txt --top 3 --sem-stopwords
```

Saída:

```
gato: 4
cachorro: 3
passaro: 2
```

## Como rodar os testes

```bash
python3 -m unittest -v
```
