NO-GO

Veredito sobre o commit 0ae40ae, como foi entregue. O achado grave já foi corrigido neste commit de revisão.

## Achados

- **grave** — frases.py:5 — `contar_frases` contava cada sinal de pontuação como uma frase: "Que?!" dava 2, "Espera... Ok." dava 4 e "Oi. !" dava 2. Isso também distorcia `media_palavras`. Corrigido: sinais seguidos agora são agrupados e segmentos sem texto são descartados. Testes acrescentados: `test_pontuacao_repetida_conta_uma_frase` e `test_pontuacao_solta_nao_conta_frase` (test_frases.py).
- **medio** — frases.py:5 — o ponto decimal é lido como fim de frase: "Custa 3.5 reais." conta 2 frases. Não foi corrigido.
- **medio** — frases.py:13 — `media_palavras` soma as palavras do trecho final sem pontuação, mas não conta esse trecho como frase: "Oi. tchau tchau" dá 3.0. Não foi corrigido.
- **leve** — frases.py:13 — `\w+` separa palavras com hífen ou apóstrofo ("guarda-chuva" vira 2 palavras). Não foi corrigido.
- **leve** — test_frases.py — faltavam testes de pontuação repetida, números decimais e texto final sem pontuação.
