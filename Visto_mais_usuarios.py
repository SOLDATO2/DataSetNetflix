import pandas as pd


def Visto_mais_usuarios(df):
    # Filtra os títulos que não são trailers, hooks ou clipes
    df = df[~df['Supplemental Video Type'].str.contains('TRAILER|HOOK|TEASER_TRAILER', na=False)]

    # Encontre os títulos duplicados
    duplicados = df[df.duplicated(subset=['Title', 'Profile Name'], keep=False)]

    # Conte quantos usuários viram cada título duplicado
    quantidade_usuarios = duplicados.groupby('Title')['Profile Name'].nunique()

    # Filtra apenas os titulos vistos por mais de um usuário
    multiplos_usuarios = quantidade_usuarios[quantidade_usuarios > 1]

    # Itere pelos títulos e imprima as informações
    for titulo, quantidade in multiplos_usuarios.items():
        usuarios = df[df['Title'] == titulo]['Profile Name'].unique()
        
        print(f"Título: {titulo}")
        print(f"Quantidade de usuários: {quantidade}")
        print(f"Usuários: {', '.join(usuarios)}\n")
