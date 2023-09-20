# Executando o Código em Ambiente Hadoop

Este código foi adaptado para ser executado em um ambiente Hadoop usando o Hadoop Streaming. As seguintes modificações foram feitas para tornar o código compatível com o Hadoop:

## Modificações no Código

1. Importações de bibliotecas foram adaptadas para o ambiente Hadoop.
2. O código foi reestruturado para seguir o formato MapReduce, com funções `mapper` e `reducer`.
3. A entrada e a saída foram modificadas para usar os fluxos padrão (stdin e stdout) do Hadoop Streaming.

## Como Executar

Para executar o código em um cluster Hadoop, siga estas etapas:

1. Faça upload do arquivo de entrada para o HDFS (Hadoop Distributed File System):

   ```bash
   hadoop fs -put seuarquivo.txt /input/
    ```

2. Execute o trabalho MapReduce usando o Hadoop Streaming:

    ```bash
    hadoop jar hadoop-streaming.jar \
    -input /input/seuarquivo.txt \
    -output /output/ \
    -mapper mapper.py \
    -reducer reducer.py \
    -file mapper.py \
    -file reducer.py
    ```

3. Verifique a saída gerada no HDFS

    ```bash
    hadoop fs -cat /output/part-*
    ```

## Observações: 

1. Lendo dados de entrada (stdin):
Em seu script Python (no mapper ou reducer), você pode usar a função sys.stdin para ler dados da entrada padrão. Aqui está um exemplo simplificado de um script Python que lê linhas de texto da entrada padrão:

    ```bash
    import sys

    for line in sys.stdin:
        # Processar a linha de entrada
        # Exemplo: dividir a linha em palavras
        words = line.strip().split()
        for word in words:
            # Emitir resultados para stdout
            print(f'{word}\t1')  # Saída no formato chave-valor
    ```

    Neste exemplo, cada linha de entrada é lida da entrada padrão usando um loop for line in sys.stdin. Você pode processar a linha como necessário e emitir resultados para stdout usando print. A saída deve estar no formato chave-valor, onde a chave é separada do valor por um caractere de tabulação (\t).

<br>

2. Recebendo resultados (stdout): Os resultados gerados pelo seu script Python são coletados pelo Hadoop Streaming e gravados em arquivos no HDFS. Você pode usar comandos do Hadoop para acessar esses resultados após a conclusão do trabalho MapReduce.

    Por exemplo, após a execução do trabalho, você pode usar o comando hadoop fs -cat para ler a saída do HDFS e direcionar os resultados para um arquivo local:

    ```bash
    hadoop fs -cat /output/part-* > resultados.txt
    ```

    Neste exemplo, /output é o diretório de saída configurado para o trabalho MapReduce e part-* são os arquivos de saída gerados pelo Hadoop Streaming. Os resultados são direcionados para um arquivo local chamado resultados.txt.

<br>

**Certifique-se de fornecer o arquivo de entrada real (`seuarquivo.txt`), os scripts Python adaptados (`mapper.py` e `reducer.py`), e o JAR real do Hadoop Streaming no seu ambiente. Além disso, ajuste os caminhos de entrada e saída conforme necessário. Este README fornecerá uma orientação básica para executar o código em um ambiente Hadoop.**
