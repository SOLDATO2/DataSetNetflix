import pandas as pd
import matplotlib.pyplot as plt


def Titulos_xtempo(df):
    # Converte o formato de data do Excel
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Pergunta ao usuário para quem sera o grafico
    nome = input("Nome do usuário (Elisabete, Neu, Felipe, Kids): ")

    # Pergunta ao usuário qual é o tempo máximo em minutos para buscar
    tempo_maximo = int(input("Tempo máximo de duração (em minutos): "))

    # Filtra os dados para o usuário informado
    df_usuario = df[df['Profile Name'] == nome]

    # Converte a coluna 'Duration' em minutos
    df_usuario['Duration'] = df_usuario['Duration'].apply(lambda x: int(x.split(':')[0]) * 60 + int(x.split(':')[1]))

    # Filtra os títulos vistos até o tempo máximo especificado
    df_filtrado = df_usuario[df_usuario['Duration'] <= tempo_maximo]

    # Cria um gráfico de Scatterplot (Dispersão)
    plt.scatter(df_filtrado.index, df_filtrado['Duration'], s=50, c='blue', alpha=0.7)

    # Definir os rótulos
    plt.xlabel("Índice do Título")
    plt.ylabel(f"Duração do título em minutos)")
    plt.title(f"Duração dos Títulos Vistos por {nome} até {tempo_maximo} minutos")

    # Mostrar o gráfico
    plt.show()
