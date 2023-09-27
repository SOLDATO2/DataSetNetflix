import pandas as pd
import Funcoes_fe
import Frequencia
import Titulos_xtempo
import Usuarios_viram_titulo
import Visto_mais_usuarios

df = pd.read_excel("E:\\PYTHON-VSCODE\\BD\\APIProjeto\\ViewingActivity.xlsx")

while(True):
    print("1. Frequencia - Mostrar quantidade de dias que o usuario escolhido viu algo na netflix entre um perido especifico")
    print("2. Titulos e tempo - Mostrar grafico com os titulos vistos pelo usuario escolhido até o tempo informado")
    print("3. Titulos e tempo (TODOS) - Mostra todos os usuarios que viram o titulo informado")
    print("4. Vistos por mais usuarios - Mostra os titulos vistos por mais de um usuario e quais usuarios assistiram")
    print("5. Media de tempo até uma data especifica - Mostra media de tempo vendo eps/filmes na netflix ate uma data.")
    print("6. Quantidade Episodios vistos sem repetição até uma data (TODOS) - Mostra quantidade de episodios vistos sem repetição até uma data.")
    print("7. Episodios duplicados vistos (TODOS) - Mostra Episodios/filmes que foram vistos mais de uma vez por usuario.")
    print("8. Media Tempo de um mes no ano - Mostra media de tempo gasto vendo filmes/episodios em um mes especifico de todos os anos.")
    print("9. Media Tempo (TODOS) - Mostra media de tempo TOTALIZADO de cada usuario investidos vendo Filmes/series")
    print("0. Sair")
    
    escolha = int(input("Escolha uma opcao: "))
    
    match escolha:
        case 1:
            Frequencia.Frequencia(df)

        case 2:
            Titulos_xtempo(df)
            
        case 3:
            Usuarios_viram_titulo.Usuarios_viram_titulo(df)
            
        case 4:
            Visto_mais_usuarios.Visto_mais_usuarios(df)
            
        case 5:
            Funcoes_fe.media_tempo_assistido_ate_xy(df)
           
        case 6:
            Funcoes_fe.qnt_episodios_vistos_todos_sem_rep_ate_xy(df)
           
        case 7:
            Funcoes_fe.eps_vistos_dup_todos(df)
        
        case 8:
            Funcoes_fe.media_tempo_de_mes_de_todos_anos(df)
       
        case 9:
            Funcoes_fe.media_todos(df)
         
        case 0:
            break
