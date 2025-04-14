import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configura o estilo dos gráficos do Seaborn
sns.set_style("whitegrid")

def main():
    # Carrega os dados do CSV.
    try:
        df = pd.read_csv(r"data\sugar_consumption.csv")
    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o caminho do arquivo.")
        return

    # Exibe informações básicas do DataFrame
    print("Formato do DataFrame:", df.shape)
    print("Colunas disponíveis:", df.columns.tolist())
    print("\nInformações do DataFrame:")
    print(df.info())
    print("\nEstatísticas descritivas:")
    print(df.describe())

    # Análise: Top 10 países com maior consumo médio de açúcar per capita.
    top_consumo = (df.groupby("Country")["Per_Capita_Sugar_Consumption"]
                   .mean()
                   .sort_values(ascending=False)
                   .head(10))
    print("\nTop 10 países com maior consumo médio de açúcar per capita:")
    print(top_consumo)

    # Visualização: Gráfico de barras para os 10 países com maior consumo médio.
    plt.figure(figsize=(10, 6))
    ax = top_consumo.plot(kind='bar', color='skyblue')
    plt.title("Top 10 países com maior consumo médio de açúcar per capita")
    plt.xlabel("País")
    plt.ylabel("Consumo per Capita de Açúcar (kg)")
    
    # Adiciona rótulos nos dados
    for p in ax.patches:
        ax.annotate(f'{p.get_height():.2f}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='center', 
                    fontsize=10, color='black', 
                    xytext=(0, 5), textcoords='offset points')

    plt.tight_layout()  # Ajusta o layout para evitar cortes nos textos
    plt.show()

if __name__ == "__main__":
    main()
