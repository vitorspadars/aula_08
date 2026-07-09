from etl import pipeline_calcular_kpi_de_vendas_consolidade     

pasta: str = 'data'
formatos_de_saida = ["csv", "parquet"]

pipeline_calcular_kpi_de_vendas_consolidade(pasta, formatos_de_saida)