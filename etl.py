import pandas as pd
import os
import glob

# Extract

def extrair_dados_e_consolidar(path: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(path, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total: pd.DataFrame = pd.concat(df_list, ignore_index=True)
    return df_total

# Transform
def calcular_kpi_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

# Load

def carregar_dados(df: pd.DataFrame, formato_saida: list):
    for formato in formato_saida :
        if formato == 'csv':
            df.to_csv("dados.csv", index=False)
        if formato == 'parquet':
            df.to_parquet("dados.parquet", index=False)


if __name__ == "__main__":
    pasta: str = 'data'
    data_frame = extrair_dados_e_consolidar(pasta)
    data_frame_calculado = calcular_kpi_de_vendas(data_frame)
    formatos_de_saida = ["csv", "parquet"]
    carregar_dados(data_frame_calculado, formatos_de_saida)