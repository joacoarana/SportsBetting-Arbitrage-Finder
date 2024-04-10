# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 01:46:56 2023

@author: rjara
"""

#%%
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np 

pd.set_option('display.max_columns', None)


#%%


premier_league= 'https://ar.1xbet.com/es/line/football/88637-england-premier-league'
liga_profesional= 'https://1xbet.com/es/line/football/119599-argentina-primera-division'
la_liga ='https://ar.1xbet.com/es/line/football/127733-spain-la-liga'
copa_libertadores= 'https://1xbet.com/es/line/football/142091-copa-libertadores'
serie_a='https://1xbet.com/es/line/football/110163-italy-serie-a'
prim_nacional= 'https://pba.betsson.bet.ar/apuestas-deportivas/futbol/argentina/argentina-primera-nacional'
la_liga_b= 'https://onex.bet/es/line/football/27687-spain-segunda-division'
copa_sudamericana='https://ar.1xbet.com/line/football/1528791-copa-sudamericana'
la_liga_tercera= 'https://ar.1xbet.com/line/football/2284105-spain-tercera-division-rfef'


def OneXBet(liga):
    
    response = requests.get(liga)
    soup = BeautifulSoup(response.text, 'html.parser')
    dashboard= soup.find(class_='dashboard c-events blueBack')
    bets=dashboard.find_all(class_="c-bets")
    
    pago=[]
    wins=[]
    home_away=[]
    
    for bet in bets:
        apuestas= bet.find_all('span',class_='c-bets__inner')[:3]
        for pagos in apuestas:
            pago.append(pagos.text)
           # print(pago)
        #if pago is not None:
            #print(pago)
            
    ganadores= bets[0].find_all('div')[:3]
    for ganador in ganadores:
        wins.append(ganador.text)
    
    lista_partidos= dashboard.find_all('a','c-events__name')
    for partido in lista_partidos:
        teams= partido.find_all('span','c-events__team')
        game= str(teams[0].text)+ ' - ' +str(teams[1].text) #hacer un loop
        home_away.append(game)
        #print(home_away)   
    
    df= pd.DataFrame(index= home_away, columns=wins)
    num_rows = len(home_away)
    num_cols= len(wins)
    values_array= np.array(pago).reshape(num_rows, num_cols)
    for i in range (len(df)):
        df.loc[df.index[i]]= values_array[i]
    

    # Exclude matches with specified names
    matches_to_exclude = ['Locales - Visitantes', 'Locales (Apuestas especiales) - Visitante (Apuestas especiales)']
    df = df[~df.index.isin(matches_to_exclude)]

    # Create a list of dictionaries
    games = []

    for index, row in df.iterrows():
        teams = index.split(' - ')
        game_dict = {teams[0]: float(row['1']), 'Empate': float(row['X']), teams[1]: float(row['2'])}
        games.append(game_dict)
        
    return games


#%%
# a=OneXBet(premier_league)
# print(a)

#%%


# import pandas as pd

# # Sample data (Replace this with your actual dataframe)
# data = {
#     '1': ['10.5', '1.297', '2.989', '1.363', '2.215', '3.08', '1.75', '2.636', '1.561', '3.105', '2.98', '2.636', '1.396'],
#     'X': ['5.94', '6.51', '3.62', '5.62', '3.64', '3.43', '4.19', '5.04', '7.65', '3.705', '3.725', '5.04', '5.49'],
#     '2': ['1.33', '11', '2.472', '9.65', '3.455', '2.503', '4.865', '1.968', '3.38', '2.361', '2.432', '1.968', '8.55']
# }

# df = pd.DataFrame(data, index=[
#     'Burnley - Manchester City',
#     'Arsenal - Nottingham Forest',
#     'Bournemouth - West Ham United',
#     'Brighton & Hove Albion - Luton Town',
#     'Everton - Fulham',
#     'Sheffield United - Crystal Palace',
#     'Newcastle United - Aston Villa',
#     'Locales - Visitantes',
#     'Locales (Apuestas especiales) - Visitante (Apuestas especiales)',
#     'Brentford - Tottenham Hotspur',
#     'Chelsea - Liverpool',
#     'Locales - Visitantes',
#     'Manchester United - Wolverhampton Wanderers'
# ])

# # Exclude matches with specified names
# matches_to_exclude = ['Locales - Visitantes', 'Locales (Apuestas especiales) - Visitante (Apuestas especiales)']
# df = df[~df.index.isin(matches_to_exclude)]

# # Create a list of dictionaries
# games = []

# for index, row in df.iterrows():
#     teams = index.split(' - ')
#     game_dict = {teams[0]: float(row['1']), 'Empate': float(row['X']), teams[1]: float(row['2'])}
#     games.append(game_dict)

# print(games)



