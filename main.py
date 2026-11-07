import pandas as pd

# ==========================================
# 1. EXTRAÇÃO (Extract)
# ==========================================
def extrair_dados(caminho_arquivo):
    print("Iniciando a extração dos dados...")
    df = pd.read_csv(caminho_arquivo)
    return df

# ==========================================
# 2. TRANSFORMAÇÃO (Transform)
# ==========================================
def gerar_mensagem(nome):
    return f"Olá, {nome}! Investir no seu futuro financeiro é o primeiro passo para o sucesso."

def transformar_dados(df):
    print("Transformando os dados e gerando mensagens...")
    df['Mensagem'] = df['Nome'].apply(gerar_mensagem)
    return df

# ==========================================
# 3. CARREGAMENTO (Load)
# ==========================================
def carregar_dados(df, caminho_saida):
    print(f"Salvando os dados processados em {caminho_saida}...")
    df.to_csv(caminho_saida, index=False)
    print("Processo de ETL concluído com sucesso!")

if __name__ == "__main__":
    arquivo_entrada = "clientes.csv"
    arquivo_saida = "clientes_processados.csv"

    dados_extraidos = extrair_dados(arquivo_entrada)
    dados_transformados = transformar_dados(dados_extraidos)
    carregar_dados(dados_transformados, arquivo_saida)