import pandas as pd
import matplotlib.pyplot as plt


def Frequencia(df):
    # Converte o formato de data do Excel
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Pergunta ao usuário para quem sera o grafico
    nome = input("Nome do usuário (Elisabete, Neu, Felipe, Kids): ")

    # Filtra os dados para o usuário especificado
    df_usuario = df[df['Profile Name'] == nome]

    # Filtra os dados para cada ano (2023, 2022, 2021) e divide em outros Data Frames
    df_2023 = df_usuario[(df_usuario['Start Time'] >= '2023-01-01') & (df_usuario['Start Time'] <= '2023-12-31')]
    df_2022 = df_usuario[(df_usuario['Start Time'] >= '2022-01-01') & (df_usuario['Start Time'] <= '2022-12-31')]
    df_2021 = df_usuario[(df_usuario['Start Time'] >= '2021-01-01') & (df_usuario['Start Time'] <= '2021-12-31')]

    # Conta a quantidade de dias únicos em que o usuário assistiu pelo menos um episódio em cada ano
    dias_unicos_2023 = df_2023['Start Time'].dt.date.nunique()
    dias_unicos_2022 = df_2022['Start Time'].dt.date.nunique()
    dias_unicos_2021 = df_2021['Start Time'].dt.date.nunique()

    # Cria listas com os anos e quantidades de dias únicos
    anos = ['2023', '2022', '2021']
    dias_unicos = [dias_unicos_2023, dias_unicos_2022, dias_unicos_2021]

    # Crie um gráfico de barras
    plt.bar(anos, dias_unicos)

    # Definir os rótulos
    plt.xlabel("Ano")
    plt.ylabel("Dias com pelo menos 1 episódio assistido")
    plt.title(f"Frequencia de {nome} em 2021, 2022 e 2023")

    # Mostrar o gráfico
    plt.show()
