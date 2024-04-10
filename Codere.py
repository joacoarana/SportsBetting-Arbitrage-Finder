# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 15:56:29 2023

@author: rjara
"""

#%%

import time
import pandas
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

#%%


def Codere(str_liga):
    
    ligas= {
        'eng'   : ['Inglaterra','Premier League'],
        'eng2'  : ['Inglaterra','Championship'],
        'ita'   : ['Italia', 'Serie A'],
        'ita2'  : ['Italia', 'Serie B'],
        'fra'   : ['Francia', 'Ligue 1'],
        'fra2'  : ['Francia', 'Ligue 2'],
        'esp'   : ['España', 'Primera División'],
        'esp2'  : ['España', 'Segunda División'],
        'ger'   : ['Alemania', 'Bundesliga'],
        'ger2'  : ['Alemania', 'Bundesliga 2'],
        'arg'   : ['Argentina', 'Liga Profesional'],
        'arg2'  : ['Argentina', 'Primera Nacional'],
        'wc_f'  : ['Internacional', 'FIFA Copa Mundial Femenino 2023'],
        'ucl'   : ['Clubes Internacional', 'UEFA Champions League -'],
        'sue'   : ['Suecia', 'Allsvenskan'],
        'den'   : ['Dinamarca', 'Superliga Dinamarca'],
        'est'   : ['Estonia', 'Meistriliiga'],
        'fin'   : ['Finlandia', 'Veikkausliiga'],
        'tur'   : ['Turquía', 'Super Lig']
        
        
        }
    
    url='https://m.caba.codere.bet.ar/deportes/#/PaisLigaPage'
        
    # s = Service(ChromeDriverManager().install())
        
    def get_new_options():
            options = webdriver.ChromeOptions()
            prefs = {"profile.managed_default_content_settings.images": 2}
            options.add_experimental_option("prefs", prefs)
            options.add_argument("--mute-audio")
            prefs = {"profile.default_content_setting_values.notifications": 2}
            options.add_experimental_option("prefs", prefs)
            options.add_argument("start-maximized")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument('--disable-popup-blocking')
            options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
            options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36")
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-blink-features=AutomationControlled")
            
            return options
        
    driver = webdriver.Chrome(options=get_new_options())
    driver.maximize_window()
    action = ActionChains(driver)
    driver.get(url)
    time.sleep(7)
    
    cookies= driver.find_element(By.XPATH,"//span[contains(text(), 'OK')]")
    cookies.click()
    time.sleep(1)
    futbol= driver.find_element(By.XPATH, "//p[contains(text(),'Fútbol')]")
    futbol.click()       
    # except:
    #     try:
    #         time.sleep(0.3)
    #         futbol= driver.find_elements(By.XPATH, "//p[contains(text(),'Fútbol')]")
    #         futbol.click()
    #     except:
    #         pass
        
    time.sleep(1)
    try:
        country= driver.find_element(By.XPATH, f"//p[contains(text(),'{ligas[str_liga][0]}')]")
        country.click()
        time.sleep(0.1)
    except:
        try:
            country= driver.find_element(By.XPATH, f"//p[contains(text(),'{ligas[str_liga][0]}')]")
            country.click()
            time.sleep(0.1)
        except:
            pass

    try:
        
        league= country.find_element(By.XPATH,f"(//p[contains(text(),'{ligas[str_liga][1]}')])")
        league.click()
    except:
        try:
            time.sleep(0.1)
            league= country.find_element(By.XPATH,f"(//p[contains(text(),'{ligas[str_liga][1]}')])")
            league.click()
        except:
            pass
    time.sleep(3)
    
    nn = driver.find_elements(By.TAG_NAME, 'sb-grid-item')
    soup=[]
    for n in nn:
        soup.append(BeautifulSoup(n.get_attribute('innerHTML'), 'html.parser'))
    
    driver.quit()
    
    games = []
    for s in soup:
        dd = {}
        
        teams       =  s.find_all(class_='sb-grid-item--title')
        equipos_n   = [teams[0].text, 'Empate', teams[1].text]  #con \n
        equipos     = [element.strip().replace('\n', '') for element in equipos_n]
        
        odds    = s.find_all(class_='sb-button--subtitle')[:3]
        
        for i in range(len(odds)):
            odd_str         = odds[i].text
            odd             = odd_str.replace(',','.')
            dd[equipos[i]]  = float(odd)
        # print(dd)
        games.append(dd)   
        
    games = [game for game in games if game] # A lo BOCA
    modified_games = [{k: v for i, (k, v) in enumerate(game.items()) if i < 3} for game in games]
    dictionaries_with_three_keys = [game for game in modified_games if len(game) == 3]
    return dictionaries_with_three_keys

#%%
#Codere('eng')




