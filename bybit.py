# -*- coding: utf-8 -*-
"""Crypto Main.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1MqHKQrWn-q9jirM4Qb9clILIwt84GRGU
### Initialize
##### Installs
"""

# Commented out IPython magic to ensure Python compatibility.
import sys 
# %load_ext autotime

"""##### Imports"""

from selenium import webdriver
import bs4
import requests
from bs4 import BeautifulSoup
import pandas as pd
from zipfile import ZipFile
import warnings
import re
import pandas as pd
from datetime import date
from datetime import datetime
import time
warnings.filterwarnings("ignore", category=DeprecationWarning)
import dropbox
import os
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

'''
chrome_options = webdriver.ChromeOptions() 
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
'''

#### Heroku Driver

chrome_options= webdriver.ChromeOptions()
chrome_options.binary_location = os.getenv('GOOGLE_CHROME_BIN')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')

#driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
driver = webdriver.Chrome(executable_path=os.getenv('CHROME_EXECUTABLE_PATH'), options=chrome_options)

"""##### Declarations"""

global nerve_fail
global sushi_fail
global adm_fail
global mirror_fail
global convex_fail
global raydium_fail
global balancer_fail
global bybit_fail
global pancake_fail
global traderjoe_fail

nerve_fail=0
sushi_fail=0
adm_fail=0
mirror_fail=0
convex_fail=0
raydium_fail=0
balancer_fail=0
bybit_fail=0
pancake_fail=0
traderjoe_fail=0

date_time_now=str(datetime.now())[:16]



def delete_cache():
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(2)
    driver.get('chrome://settings/clearBrowserData') # for old chromedriver versions use cleardriverData
    time.sleep(2)
    actions = ActionChains(driver) 
    actions.send_keys(Keys.TAB * 3 + Keys.DOWN * 3) # send right combination
    actions.perform()
    time.sleep(2)
    actions = ActionChains(driver) 
    actions.send_keys(Keys.TAB * 4 + Keys.ENTER) # confirm
    actions.perform()
    time.sleep(5) # wait some time to finish
    driver.close() # close this tab
    driver.quit() # switch back

    
def initialize():
  global nerve_fail
  global sushi_fail
  global adm_fail
  nerve_fail=0
  sushi_fail=0
  adm_fail=0
  try:
    delete_cache()
  except:
    pass
  chrome_options= webdriver.ChromeOptions()
  chrome_options.binary_location = os.getenv('GOOGLE_CHROME_BIN')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument('--disable-gpu')
  #driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
  driver = webdriver.Chrome(executable_path=os.getenv('CHROME_EXECUTABLE_PATH'), options=chrome_options)



def bybit():
  print("Started bybit")
  url="https://quickswap.exchange/#/quick"
  import time
  global bybit_fail
  chrome_options.add_argument("--start-maximized")
  try:
       
    chrome_options.add_argument('--no-sandbox') 
    chrome_options.add_argument('--disable-dev-shm-usage') 
    driver = webdriver.Chrome(executable_path=os.getenv('CHROME_EXECUTABLE_PATH'), options=chrome_options)

    SCROLL_PAUSE_TIME = 4
    driver.set_window_size(1024, 600)
    driver.maximize_window()
    WebDriverWait(driver, SCROLL_PAUSE_TIME)
    driver.get(url)
    time.sleep(2)
    last_height = 0
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    while True:
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
      time.sleep(SCROLL_PAUSE_TIME)
      new_height = driver.execute_script("return document.body.scrollHeight")
      if new_height == last_height:
          break
      last_height = new_height


    page1 = driver.execute_script('return document.body.innerHTML')
    soup1 = BeautifulSoup(''.join(page1), 'html.parser')
    web_data=soup1
    print(web_data.prettify())

    main_list=web_data.find_all( "div" , class_='pnr__item pnr__item-column funding-rate help-cursor')
    main_dict=[]
    for i in main_list:
        roww=i
        record=[]
        record.append(roww.find('div',class_='pnr__item-content').contents[0].contents[0])
        record.append(roww.find('div',class_='pnr__item-content').contents[1].contents[0])
        main_dict.append(record) 
    df = pd.DataFrame(main_dict, columns = ['unPredicted','predicted'])
    #print("Extracted in ",nerve_fail+1,"attempts")
    print("Extracted ",bybit_fail+1," records")
    df.to_csv('bybit.csv')
    print(soup1)
    return df
    print("Extracted in ",bybit_fail+1,"attempts")
    

  except:
    bybit_fail=bybit_fail+1
    print('Failed ',bybit_fail,' times')
    try:
      initialize()
      
    except:
      pass
    if bybit_fail<4:
      bybit()
    else:
      print('Error in bybit')
      exit()

      


  return df


print(bybit())
