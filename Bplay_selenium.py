# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 21:03:24 2023

@author: rjara
"""

#%%

import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

pd.set_option('display.max_columns', None)
#%%BPLAY

path = ""

url_eng = 'https://deportespba.bplay.bet.ar/competicion/94-premier-league'
url_fra = 'https://deportespba.bplay.bet.ar/competicion/96-ligue-1'
# Load the webpage
def BPlay(url):
    
    chrome_options = Options()
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options= chrome_options)
    
    driver.get(url)
    time.sleep(1)
    #print(driver.page_source)
    
    partidos=driver.find_elements(By.CLASS_NAME,"odds-box")
    
    lista_partidos=[]
    
    for partido in partidos:
        game=[]
        events_odds=partido.find_elements(By.CLASS_NAME, 'odd')
        
        for event in events_odds:
            game.append(event.text)
        
        lista_partidos.append(game)
    
    games = []
    
    for item in lista_partidos:
        if len(item) == 3:
            game = {}
            for element in item:
                parts = element.split('\n')
                if len(parts) == 2 and parts[0] and parts[1]:
                    team, odds = parts
                    try:                        
                        game[team] = float(odds)
                    except:
                        game[team]= 1
            if game:
                games.append(game)
    driver.quit()
    return games
    


#%%
