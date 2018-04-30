# Hadoop

## listar arquivos
hadoop fs -ls

## Colocar um arquivo no HDFS
hadoop fs -put ARQUIVO

## executar o hadoop 
### PATH pode ser /usr/lib/hadoop_version_mapreduce/contrib/streaming/hadoop-streaming-version.jar 
hadoop jar PATH -mapper mapper.py - reducer reducer.py -file mapper.py -file reducer.py -input myinput -output job_output

- o resultado será uma pasta com nome job_output contendo 3 arquivos, onde o arquivo part-00000 é o resultado que obtivemos.

## abrir um arquivo completamente
hadoop fs -cat job_output/part-00000

## abrir somente as primeiras linhas
hadoop fs -head job_output/part-00000

## abrir somente as ultimas linhas
hadoop fs -tail job_output/part-00000

## para exportar um resultado
hadoop fs -get job_output/part-00000 nome_do_arquivo.txt

## Renomear
hadoop fs -mv ARQUIVO NOVO_NOME

## Remover
hadoop fs -rm ARQUIVO

## Criar pastas
hadoop fs -mkdir PASTA

## Colocar um arquivo nessa pasta
hadoop fs -put ARQUIVO PASTA
