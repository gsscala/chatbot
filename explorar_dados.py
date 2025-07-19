# explorar_dados.py
import pandas as pd


def load_taco_data(filepath='database/alimentos.csv'):
    """Carrega os dados nutricionais da TACO de um arquivo CSV para um DataFrame pandas."""
    try:
        # Especificando o separador ';', já que o padrão do Pandas é ','
        df = pd.read_csv(filepath, sep=';', index_col='Descrição dos alimentos')
        print("Dados da TACO carregados com sucesso.")
        return df
    except FileNotFoundError:
        print(f"Erro: O arquivo '{filepath}' nao foi encontrado. Verifique se ele está na pasta 'data'.")
        return None
    except KeyError:
        print(f"Erro: A coluna 'Descrição dos alimentos' não foi encontrada. Verifique o arquivo CSV.")
        return None


def get_food_info(df, food_name):
    """Recupera e imprime informacoes nutricionais para um alimento especifico."""
    if df is None:
        return

    try:
        # A busca precisa ser exata com o nome no índice
        food_series = df[df.index.str.lower() == food_name.lower()]

        if not food_series.empty:
            # Pega o nome real do índice para exibir corretamente (com maiúsculas/minúsculas originais)
            actual_food_name = food_series.index[0]
            print(f"\nInformacoes Nutricionais para: {actual_food_name}")
            print("-" * 40)
            # Exibe nutrientes chave
            print(f"Energia: {food_series['Energia (kcal)'].values[0]} kcal")
            print(f"Proteína: {food_series['Proteína (g)'].values[0]} g")
            print(f"Lipídeos: {food_series['Lipídeos (g)'].values[0]} g")
            print(f"Carboidrato: {food_series['Carboidrato (g)'].values[0]} g")
            print(f"Fibra Alimentar: {food_series['Fibra Alimentar (g)'].values[0]} g")
        else:
            print(f"\nAlimento '{food_name}' nao encontrado na base de dados.")
    except Exception as e:
        print(f"Ocorreu um erro ao buscar o alimento: {e}")


if __name__ == "__main__":
    # 1. Usando o caminho relativo
    taco_df = load_taco_data(filepath='database/alimentos.csv')

    if taco_df is not None:
        # 2. Usando os nomes exatos do banco de dados (com acentuação)
        get_food_info(taco_df, 'Arroz, integral, cozido')
        get_food_info(taco_df, 'Limão, cravo, suco')
        get_food_info(taco_df, 'Biscoito, doce, wafer, recheado de morango')
        get_food_info(taco_df, 'Alimento Inexistente')
