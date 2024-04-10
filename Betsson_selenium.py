# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 15:47:33 2023

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
#%%
url_fra= 'https://pba.betsson.bet.ar/apuestas-deportivas/futbol/espana/espana-la-liga'

def Betsson(url):
    
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

    action = ActionChains(driver)
    driver.get(url)
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="onetrust-accept-btn-handler"]').click()
    time.sleep(2)
    
    try:
        for i in range(1, 8):
            action.move_to_element(driver.find_elements(By.XPATH, f'//span[@class="obg-m-events-master-detail-header-title"]')[i]).perform()
            time.sleep(1.5)
    except:
        pass
    
    action.move_to_element(driver.find_element(By.XPATH, '//obg-lazy-image[@test-id="img_svg-facebook"]')).perform()
    time.sleep(3)
    
    nn = driver.find_elements(By.TAG_NAME, 'obg-event-row-container')
    # print(len(nn))
    
    games = []
    for n in nn:
        aa = n.find_elements(By.TAG_NAME, 'obg-event-row-market-container')
        # print(len(aa))
        dd = {}
        for a in aa:
            bb = a.find_elements(By.TAG_NAME, 'obg-selection-container')
            for b in bb:
                name1 = b.find_element(By.XPATH, './/div[@class="obg-selection-content-label-wrapper"]').text.strip()
                em = b.find_element(By.TAG_NAME, 'obg-numeric-change').text.strip()
                dd[name1] = float(em)
        # print(dd)
        games.append(dd)
    games = [game for game in games if game] # A lo BOCA
    modified_games = [{k: v for i, (k, v) in enumerate(game.items()) if i < 3} for game in games]
    dictionaries_with_three_keys = [game for game in modified_games if len(game) == 3]
    driver.quit()
    return dictionaries_with_three_keys


#%%


# Betsson(url_fra)
