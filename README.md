# Trabalho de MapReduce em Python

## Identificação do Grupo
- Felipe Correia Andrade (Matrícula: 180113259)
- Mateus Brandão Teixeira (Matrícula: 180127535)
- Adrian Soares Lopes (Matrícula: 160000572)

## Explicação Resumida do Código
Este projeto consiste em um trabalho de MapReduce em Python usando o Hadoop Streaming. O objetivo é contar a ocorrência de palavras em um conjunto de documentos. O projeto inclui dois scripts Python:

- `mapper.py`: Este script faz o mapeamento dos dados, lê as linhas de texto da entrada padrão, divide-as em palavras e emite pares chave-valor para cada palavra com contagem 1.

- `reducer.py`: Este script realiza a redução dos dados, agrega a contagem de palavras e emite a contagem total de cada palavra.

Para executar o trabalho no Hadoop, foram feitas as seguintes etapas:
1. Damos permissão de execução aos scripts Python usando `chmod`.
2. Configuramos e executamos o trabalho Hadoop Streaming, especificando os scripts Python, os diretórios de entrada e saída e o JAR do Hadoop Streaming.

Este README fornece uma visão geral do projeto e das etapas realizadas para executá-lo no Hadoop.

## Referências Utilizadas
- Documentação do Hadoop: https://hadoop.apache.org/
- Documentação do Hadoop Streaming: https://hadoop.apache.org/docs/stable/hadoop-streaming/HadoopStreaming.html

