# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 13:10:47 2023

@author: rjara
"""

#%%

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np 
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

pd.set_option('display.max_columns', None)
#%%BPLAY

path = "C:/Users/rjara/OneDrive/Desktop/chromedriver_win32/chromedriver.exe"



url_eng = 'https://pba.betwarrior.bet.ar/es-ar/sports/futbol/inglaterra/premier-league'
#url_fra = ''
# Load the webpage

def BetWarrior(url):
    
    chrome_options = Options()
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    
    driver = webdriver.Chrome(options= chrome_options)
    
    driver.get(url)
    time.sleep(5)
    
    partidos=driver.find_elements(By.CLASS_NAME,"BoardContent__BoardContentCss-ktioqn-0")
    partidos.pop(-1)  # NO QUEREMOS 'APUESTAS DEL TORNEO'
    
    team_names=[]
    odds_strings=[]
    for partido in partidos:
        
        
        equipos= partido.find_elements(By.CLASS_NAME, 'PlayerInfo__PlayerInfoNameCss-ntxsbf-9')
        prob= partido.find_elements(By.CLASS_NAME, 'OutcomeOdds__OutcomeOddsCss-sc-1hzsddd-0')
                 
        for equipo in equipos:
            team_names.append(equipo.text)
            
        for odd in prob:
            odds_strings.append(odd.text)
            
    # Convert odds strings to floating-point numbers
    odds = [float(odds_str.replace(',', '.')) for odds_str in odds_strings]
    
    
    teams_with_draw = []
    
    # Pair the teams and insert 'Empate' in between
    for i in range(0, len(team_names), 2):
        teams_with_draw.append(team_names[i])
        if i + 1 < len(team_names):
            teams_with_draw.append('Empate')
            teams_with_draw.append(team_names[i + 1])
    
    
    
    games = []
    current_game = {}
    
    for i in range(0, len(teams_with_draw), 3):
        team1 = teams_with_draw[i]
        draw = teams_with_draw[i + 1]
        team2 = teams_with_draw[i + 2]
        current_game = {team1: odds[i], draw: odds[i + 1], team2: odds[i + 2]}
        games.append(current_game)
        
    games = [game for game in games if game] # A lo BOCA
    modified_games = [{k: v for i, (k, v) in enumerate(game.items()) if i < 3} for game in games]
    driver.quit()
    dictionaries_with_three_keys = [game for game in modified_games if len(game) == 3]
    return dictionaries_with_three_keys

#%%


