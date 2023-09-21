#Explicação do código

Agora, vamos explicar as modificações necessárias para viabilizar o funcionamento desses scripts no Hadoop usando o Hadoop Streaming:

Shebang line (linha de shebang): No início de cada script (mapper.py e reducer.py), é comum usar a linha de shebang (#!/usr/bin/env python) para indicar qual interpretador Python deve ser usado. Certifique-se de que essa linha esteja presente e aponte para o interpretador Python correto no seu ambiente Hadoop.

Permissões de execução: É necessário dar permissão de execução aos seus scripts Python para que o Hadoop Streaming possa executá-los. Use o comando chmod para isso:

```bash
Copy code
chmod +x mapper.py
chmod +x reducer.py
Configuração do trabalho Hadoop: Ao configurar e executar o trabalho Hadoop Streaming, você precisa especificar os scripts Python e os diretórios de entrada e saída. Suponha que seus arquivos de entrada estejam em um diretório chamado /input e você deseje enviar a saída para /output. O comando para executar o trabalho seria semelhante a este:
```

```bash
Copy code
hadoop jar hadoop-streaming.jar \
  -input /input \
  -output /output \
  -mapper mapper.py \
  -reducer reducer.py \
  -file mapper.py \
  -file reducer.py  
```

Certifique-se de substituir hadoop-streaming.jar pelo caminho real do JAR do Hadoop Streaming e ajustar os caminhos de entrada e saída conforme necessário.

Formato de entrada e saída: Seu código Python deve estar preparado para ler dados da entrada padrão (stdin) e gravar resultados na saída padrão (stdout). No caso do mapper, cada linha de entrada é lida da entrada padrão, e no caso do reducer, os resultados são escritos na saída padrão.