#!/usr/bin/env python

import sys
import re

# Função de mapeamento (map)
def mapper():
    # Lê a entrada da linha de comando
    for line in sys.stdin:
        # Divide a linha em palavras
        words = re.findall(r'\b\w+\b', line)

        # Emite a contagem de cada palavra
        for word in words:
            print(f'{word}\t1')

if __name__ == "__main__":
    mapper()
