# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 20:36:54 2023

@author: rjara
"""

#%%

import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
#%%


def Sportsbet(url):
    
    chrome_options = Options()
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options= chrome_options)
    wait     = WebDriverWait(driver, 6)
    driver.get(url)
    
    try:       
        element     = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'MatchesContainer__MatchesWrapper-sc-nepsbu-0')))
        nn          = driver.find_elements(By.CLASS_NAME,"grid__EventListBodyWrapper-sc-l1d0h4-0")       
        partidos    = []
        for n in nn:
            partidos.append(BeautifulSoup(n.get_attribute('innerHTML'), 'html.parser'))
        
        #print(nn)
        driver.quit()
        
        games=[]        
        for p in partidos:
            dd = {}
            event=p.find(class_='grid__StyledEventInfo-sc-pldpgc-0')
            teams= event.find_all('a')
            
            equipos = [teams[0].text, 'Empate', teams[1].text]
            
            odds_grid= p.find(class_='grid__StyledMarket1X2-sc-pldpgc-1')
            odds= odds_grid.find_all('p')
            
            for i in range(len(odds)):
                odd         = odds[i].text
                dd[equipos[i]]  = float(odd)
            # print(dd)
            games.append(dd)   
        games = [game for game in games if game] # A lo BOCA
        modified_games = [{k: v for i, (k, v) in enumerate(game.items()) if i < 3} for game in games]
        dictionaries_with_three_keys = [game for game in modified_games if len(game) == 3]
        
    except:
        print("Element not found or took too long to load")
    
    return dictionaries_with_three_keys

#%%

# lol = Sportsbet('https://sportsbet.io/es/sports/soccer/england/premier-league/matches')
# print(lol)


