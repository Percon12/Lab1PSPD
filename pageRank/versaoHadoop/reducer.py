#!/usr/bin/env python

import sys

# Função de redução (reduce)
def reducer():
    current_word = None
    current_count = 0

    # Processa as linhas de entrada
    for line in sys.stdin:
        word, count = line.strip().split('\t')

        # Verifica se a palavra mudou
        if current_word == word:
            current_count += int(count)
        else:
            # Emite a contagem da palavra anterior
            if current_word:
                print(f'{current_word}\t{current_count}')

            current_word = word
            current_count = int(count)

    # Emite a última palavra
    if current_word:
        print(f'{current_word}\t{current_count}')

if __name__ == "__main__":
    reducer()
