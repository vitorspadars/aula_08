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


if __name__ == "__main__":
    pasta = 'data'
    data_frame = extrair_dados_e_consolidar(pasta)
    print(calcular_kpi_de_vendas(data_frame))