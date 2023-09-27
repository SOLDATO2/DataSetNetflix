import pandas as pd
import matplotlib.pyplot as plt


#terminal
def media_tempo_assistido_ate_xy(df): #ok
    escolha = int(input("Escolha um usuario:\n1. Felipe\n2. Elisabete\n3. Neu \n4. Kids\n"))
    usuario = ""
    data_inicial = pd.to_datetime(input("Digite uma data inicial (ex: 2021-10-12): "))
    data_final = pd.to_datetime(input("Digite uma data final (ex: 2021-10-14): ")) + pd.Timedelta(days=1)
    match escolha:
        case 1:
            usuario = "Felipe"
        case 2:
            usuario = "Elisabete"
        case 3:
            usuario = "Neu"
        case 4:
            usuario = "Kids"
     
    if(data_inicial == data_final):
        df_filtrada = df.loc[(df["Start Time"] == data_final) & (df["Profile Name"] == usuario)]
    else:
        df_filtrada = df.loc[(pd.to_datetime(df["Start Time"]) >= data_inicial) & (pd.to_datetime(df["Start Time"]) <= data_final) & (df["Profile Name"] == usuario)]
    
    tempo = pd.to_timedelta("00:00:00") 
    dias = 0
    dias_registrados = []
    for coluna, linha in df_filtrada.iterrows():
        if (linha["Supplemental Video Type"] != "HOOK") and (linha["Supplemental Video Type"] != "TRAILER") and (linha["Supplemental Video Type"] != "TEASER_TRAILER"):
            
            if (pd.to_datetime(linha["Start Time"]).date()) not in dias_registrados: 
                dias_registrados.append(pd.to_datetime(linha["Start Time"]).date())
                dias+= 1
                
            tempo = tempo + pd.to_timedelta(linha["Duration"])
     
    tempo = tempo.total_seconds() 
    segundos = tempo
    horas = segundos/3600
    media = horas/dias
    media = media * 60
    
    
    print(f"Média de {data_final} até {data_final - pd.Timedelta(days=1)}: {media} minutos")

#grafico
def qnt_episodios_vistos_todos_sem_rep_ate_xy(df): #ok
    
    data_inicial = pd.to_datetime(input("Digite uma data inicial (ex: 2021-10-12): "))
    data_final = pd.to_datetime(input("Digite uma data final (ex: 2021-10-14): ")) + pd.Timedelta(days=1)
    
            
    if(data_inicial == data_final):
        df_filtrada_felipe = df.loc[(df["Start Time"] == data_final) & (df["Profile Name"] == "Felipe")]
        df_filtrada_elisabete = df.loc[(df["Start Time"] == data_final) & (df["Profile Name"] == "Elisabete")]
        df_filtrada_neu = df.loc[(df["Start Time"] == data_final) & (df["Profile Name"] == "Neu")]
        df_filtrada_kids = df.loc[(df["Start Time"] == data_final) & (df["Profile Name"] == "Kids")]
    else:
        df_filtrada_felipe = df.loc[(pd.to_datetime(df["Start Time"]) >= data_inicial) & (pd.to_datetime(df["Start Time"]) <= data_final) & (df["Profile Name"] == "Felipe")]
        df_filtrada_elisabete = df.loc[(pd.to_datetime(df["Start Time"]) >= data_inicial) & (pd.to_datetime(df["Start Time"]) <= data_final) & (df["Profile Name"] == "Elisabete")]
        df_filtrada_neu = df.loc[(pd.to_datetime(df["Start Time"]) >= data_inicial) & (pd.to_datetime(df["Start Time"]) <= data_final) & (df["Profile Name"] == "Neu")]
        df_filtrada_kids = df.loc[(pd.to_datetime(df["Start Time"]) >= data_inicial) & (pd.to_datetime(df["Start Time"]) <= data_final) & (df["Profile Name"] == "Kids")]
   
    episodios_vistos_felipe = 0
    episodios_registrados_felipe = [] 
    for coluna, linha in df_filtrada_felipe.iterrows():
        if (linha["Supplemental Video Type"] != "HOOK") and (linha["Supplemental Video Type"] != "TRAILER") and (linha["Supplemental Video Type"] != "TEASER_TRAILER"):
            if linha["Title"] not in episodios_registrados_felipe:
                episodios_vistos_felipe += 1
                episodios_registrados_felipe.append(linha["Title"])
    
    episodios_vistos_elisabete = 0
    episodios_registrados_elisabete = [] 
    for coluna, linha in df_filtrada_elisabete.iterrows():
        if (linha["Supplemental Video Type"] != "HOOK") and (linha["Supplemental Video Type"] != "TRAILER") and (linha["Supplemental Video Type"] != "TEASER_TRAILER"):
            if linha["Title"] not in episodios_registrados_elisabete:
                episodios_vistos_elisabete += 1
                episodios_registrados_elisabete.append(linha["Title"])

    episodios_vistos_neu = 0
    episodios_registrados_neu = [] 
    for coluna, linha in df_filtrada_neu.iterrows():
        if (linha["Supplemental Video Type"] != "HOOK") and (linha["Supplemental Video Type"] != "TRAILER") and (linha["Supplemental Video Type"] != "TEASER_TRAILER"):
            if linha["Title"] not in episodios_registrados_neu:
                episodios_vistos_neu += 1
                episodios_registrados_neu.append(linha["Title"])
    
    episodios_vistos_kids = 0
    episodios_registrados_kids = [] 
    for coluna, linha in df_filtrada_kids.iterrows():
        if (linha["Supplemental Video Type"] != "HOOK") and (linha["Supplemental Video Type"] != "TRAILER") and (linha["Supplemental Video Type"] != "TEASER_TRAILER"):
            if linha["Title"] not in episodios_registrados_kids:
                episodios_vistos_kids += 1
                episodios_registrados_kids.append(linha["Title"])
                
                
    usuarios = ["Felipe","Elisabete","Neu","Kids"]
    episodios_vistos = [episodios_vistos_felipe, episodios_vistos_elisabete, episodios_vistos_neu, episodios_vistos_kids]
    
    plt.barh(usuarios, episodios_vistos, color="blue")
    plt.title(f"Episodios vistos entre {data_inicial.date()} e {data_final.date() - pd.Timedelta(days=1)} ")
    plt.xlabel("Episodios vistos")
    plt.ylabel("Usuário")
    plt.show()
     
#grafico
def eps_vistos_dup_todos(df):#ok
    
     
    
    df_felipe = df.loc[(df["Profile Name"] == "Felipe") & (df["Supplemental Video Type"] != "HOOK") & (df["Supplemental Video Type"] != "TRAILER") & (df["Supplemental Video Type"] != "TEASER_TRAILER")]
    df_neu = df.loc[(df["Profile Name"] == "Neu") & (df["Supplemental Video Type"] != "HOOK") & (df["Supplemental Video Type"] != "TRAILER") & (df["Supplemental Video Type"] != "TEASER_TRAILER")]
    df_elisabete = df.loc[(df["Profile Name"] == "Elisabete") & (df["Supplemental Video Type"] != "HOOK") & (df["Supplemental Video Type"] != "TRAILER") & (df["Supplemental Video Type"] != "TEASER_TRAILER")]
    df_kids = df.loc[(df["Profile Name"] == "Kids") & (df["Supplemental Video Type"] != "HOOK") & (df["Supplemental Video Type"] != "TRAILER") & (df["Supplemental Video Type"] != "TEASER_TRAILER")]

    episodio_ou_filme = input("Digite o nome do episodio/filme para verificar quantas vezes foi visto: ")
    qnt_visto_felipe = (df_felipe['Title'].str.lower() == episodio_ou_filme.lower()).sum()
    qnt_visto_neu = (df_neu['Title'].str.lower() == episodio_ou_filme.lower()).sum()
    qnt_visto_elisabete = (df_elisabete['Title'].str.lower() == episodio_ou_filme.lower()).sum()
    qnt_visto_kids = (df_kids['Title'].str.lower() == episodio_ou_filme.lower()).sum()
    
    usuarios = ["Felipe", "Elisabete", "Neu", "Kids"]
    quantidades = [qnt_visto_felipe, qnt_visto_elisabete, qnt_visto_neu, qnt_visto_kids]
    
    plt.barh(usuarios,quantidades, color="blue")
    plt.xlabel("Quantidade de vezes")
    plt.ylabel("Episódio/Filme")
    plt.title("Episodios vistos mais de uma vez")
    plt.show()
    
#grafico
def media_tempo_de_mes_de_todos_anos(df): #ok
    mes_ano = int(input("Digite o mês (1-12): "))
    escolha = int(input("Escolha um usuario:\n1. Felipe\n2. Elisabete\n3. Neu \n4. Kids\n"))
    usuario = ""
    
    match escolha:
        case 1:
            usuario = "Felipe"
        case 2:
            usuario = "Elisabete"
        case 3:
            usuario = "Neu"
        case 4:
            usuario = "Kids"
   
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    
   
    df["Duration"] = pd.to_timedelta(df["Duration"]).dt.total_seconds() / 60
    
    
    df_filtrada = df.loc[(df["Start Time"].dt.month == mes_ano) & (df["Profile Name"] == usuario) & (df["Supplemental Video Type"] != "HOOK") & (df["Supplemental Video Type"] != "TRAILER") & (df["Supplemental Video Type"] != "TEASER_TRAILER")]
    
   
    media_por_ano_mes = df_filtrada.groupby(df_filtrada["Start Time"].dt.strftime("%Y-%m"))["Duration"].mean()
    
    
    plt.barh(media_por_ano_mes.index, media_por_ano_mes.values)
    plt.title(f"Média de tempo gasto no mês '{mes_ano}' de todos os anos")
    plt.xlabel("Minutos")
    plt.ylabel("Ano-mês")
    plt.gca().invert_yaxis()  
    plt.show()
    
#grafico
def media_todos(df):# ok
    
    df_filtrada_felipe = df.loc[(df["Profile Name"] == "Felipe") & (df["Supplemental Video Type"] != "HOOK") & (df["Supplemental Video Type"] != "TRAILER") & (df["Supplemental Video Type"] != "TEASER_TRAILER")]
    df_filtrada_elisabete = df.loc[(df["Profile Name"] == "Elisabete") & (df["Supplemental Video Type"] != "HOOK") & (df["Supplemental Video Type"] != "TRAILER") & (df["Supplemental Video Type"] != "TEASER_TRAILER")]
    df_filtrada_neu = df.loc[(df["Profile Name"] == "Neu") & (df["Supplemental Video Type"] != "HOOK") & (df["Supplemental Video Type"] != "TRAILER") & (df["Supplemental Video Type"] != "TEASER_TRAILER")]
    df_filtrada_kids = df.loc[(df["Profile Name"] == "Kids") & (df["Supplemental Video Type"] != "HOOK") & (df["Supplemental Video Type"] != "TRAILER") & (df["Supplemental Video Type"] != "TEASER_TRAILER")]

    tempo = pd.to_timedelta("00:00:00")
    meses_registrados = []
    meses = 0
    for coluna, linha in df_filtrada_felipe.iterrows():
        
        if (pd.to_datetime(linha["Start Time"]).date()) not in meses_registrados:
            meses+= 1
            meses_registrados.append(pd.to_datetime(linha["Start Time"]).date())
        tempo = tempo + pd.to_timedelta(linha["Duration"])
     
    tempo = tempo.total_seconds() 
    segundos = tempo
    horas = segundos/3600
    media = horas/meses
    media_felipe = media * 60
    
    tempo = pd.to_timedelta("00:00:00")
    meses_registrados = []
    meses = 0
    for coluna, linha in df_filtrada_elisabete.iterrows():
        
        if (pd.to_datetime(linha["Start Time"]).date()) not in meses_registrados:
            meses+= 1
            meses_registrados.append(pd.to_datetime(linha["Start Time"]).date())
        tempo = tempo + pd.to_timedelta(linha["Duration"])
     
    tempo = tempo.total_seconds() 
    segundos = tempo
    horas = segundos/3600
    media = horas/meses
    media_elisabete = media * 60
    
    tempo = pd.to_timedelta("00:00:00")
    meses_registrados = []
    meses = 0
    for coluna, linha in df_filtrada_neu.iterrows():
        
        if (pd.to_datetime(linha["Start Time"]).date()) not in meses_registrados:
            meses+= 1
            meses_registrados.append(pd.to_datetime(linha["Start Time"]).date())
        tempo = tempo + pd.to_timedelta(linha["Duration"])
     
    tempo = tempo.total_seconds() 
    segundos = tempo
    horas = segundos/3600
    media = horas/meses
    media_neu = media * 60

    tempo = pd.to_timedelta("00:00:00")
    meses_registrados = []
    meses = 0
    for coluna, linha in df_filtrada_kids.iterrows():
        
        if (pd.to_datetime(linha["Start Time"]).date()) not in meses_registrados:
            meses+= 1
            meses_registrados.append(pd.to_datetime(linha["Start Time"]).date())
        tempo = tempo + pd.to_timedelta(linha["Duration"])
     
    tempo = tempo.total_seconds() 
    segundos = tempo
    horas = segundos/3600
    media = horas/meses
    media_kids = media * 60
    
    usuarios = ["Felipe", "Elisabete", "Neu", "Kids"]
    medias = [media_felipe, media_elisabete, media_neu, media_kids]

    plt.barh(usuarios, medias, color="blue")
    plt.xlabel("Média de Tempo (minutos)")
    plt.ylabel("Usuário")
    plt.title("Média de tempo gasto em minutos de cada usuário de todos os anos.")
    plt.show()

