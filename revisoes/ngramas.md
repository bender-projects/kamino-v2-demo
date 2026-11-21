GO

Revisão do commit 58e823e (feat: n-gramas mais frequentes). Os 17 testes passam (`python3 -m unittest -v`). README e demais arquivos intactos. A função atende ao pedido: n-gramas de palavras, sem diferenciar maiúsculas, ignorando pontuação, lista de (ngrama, contagem). Nenhum achado grave.

## Achados

- **medio** — `ngramas.py:7` — `tamanho` menor ou igual a 0 não é validado e devolve lixo sem erro: `mais_frequentes("a b c", 0)` → `[('', 4)]`; `mais_frequentes("a b c", -1)` → `[('', 4), ('a b', 1)]`. Sugestão: `raise ValueError` quando `tamanho < 1`, com teste.
- **leve** — `ngramas.py:6` — `\w+` trata `_` e dígitos como parte da palavra e divide contrações (`d'água` → `d`, `água`). É o mesmo critério de `palavras.contar`, então está consistente com o projeto; fica só registrado.
- **leve** — `test_ngramas.py:9`, `:13`, `:17`, `:25` — vários testes verificam só `resultado[0]`; não cobrem a lista completa nem o desempate (que segue a ordem da primeira ocorrência, via `Counter.most_common`).
- **leve** — `test_ngramas.py` — falta teste para `top` maior que a quantidade de n-gramas distintos e para `top=0`.
