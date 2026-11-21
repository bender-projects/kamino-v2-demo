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
- `--formato {texto,json}`: define o formato de saída (padrão: texto).
- `--min-letras N`: ignora palavras com menos de N letras (padrão: 1).

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

### Exemplo com saída em JSON

```bash
python3 palavras.py texto.txt --top 3 --sem-stopwords --formato json
```

Saída:

```json
[{"palavra": "gato", "contagem": 4}, {"palavra": "cachorro", "contagem": 3}, {"palavra": "passaro", "contagem": 2}]
```

## Como rodar os testes

```bash
python3 -m unittest -v
```
