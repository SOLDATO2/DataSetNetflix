import pandas as pd


def Usuarios_viram_titulo(df):
    # Recebe o nome do titulo para buscar
    titulo_procurado = input("Informe o título para buscar: ")

    # Filtrar as linhas que contem o título informado
    titulos_filtrados = df[df['Title'].str.contains(titulo_procurado, na=False)]

    # Filtrar as linhas que não possuem os valores 'HOOK', 'TRAILER' ou 'TEASER_TRAILER' na coluna 'Supplemental Video Type'
    titulos_filtrados = titulos_filtrados[~titulos_filtrados['Supplemental Video Type'].isin(['HOOK', 'TRAILER', 'TEASER_TRAILER'])]

    # Identifica os nomes dos usuário associados
    usuarios_assistiram = titulos_filtrados['Profile Name'].unique()

    # Mostra os usuários que assistiram ao título
    if len(usuarios_assistiram) > 0:
        print(f"Usuários que assistiram a '{titulo_procurado}':")
        for usuario in usuarios_assistiram:
            print(usuario)
    else:
        print(f"Nenhum usuário assistiu a '{titulo_procurado}'.")
