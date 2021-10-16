# -*- coding: utf-8 -*-
"""Crypto Scraper.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aptKZMBMxdJoNQaKVJNcEnJ60nH9Dzgo

#### Imports
"""

# Commented out IPython magic to ensure Python compatibility.

import sys 
import os
from selenium import webdriver
import bs4
import requests
from bs4 import BeautifulSoup
import pandas as pd

from zipfile import ZipFile
import warnings
import re
import pandas as pd
import time
warnings.filterwarnings("ignore", category=DeprecationWarning)
# %load_ext autotime
print('Ready')

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
chrome_options = webdriver.ChromeOptions() 
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(ChromeDriverManager().install())

"""#### Nerve.Fi"""

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = "https://nerve.fi/pools"

'''
option = webdriver.ChromeOptions()

# You will need to specify the binary location for Heroku 
option.binary_location = os.getenv('GOOGLE_CHROME_BIN')

option.add_argument("--headless")
option.add_argument('--disable-gpu')
option.add_argument('--no-sandbox')
browser = webdriver.Chrome(executable_path=os.getenv('CHROME_EXECUTABLE_PATH'), options=chrome_options)
'''

#Selenium
chrome_options= webdriver.ChromeOptions()
chrome_options.binary_location = os.getenv('GOOGLE_CHROME_BIN')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')

#driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
driver = webdriver.Chrome(executable_path=os.getenv('CHROME_EXECUTABLE_PATH'), options=chrome_options)



driver.get(url)
SCROLL_PAUSE_TIME = 3
WebDriverWait(driver, SCROLL_PAUSE_TIME)

last_height = driver.execute_script("return document.body.scrollHeight")

driver.get_cookies()
import time
while True:

  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

  time.sleep(SCROLL_PAUSE_TIME)

  new_height = driver.execute_script("return document.body.scrollHeight")
  if new_height == last_height:
      break
  last_height = new_height
  print(last_height)
page1 = driver.execute_script('return document.body.innerHTML')
soup1 = BeautifulSoup(''.join(page1), 'html.parser')

#soup1.prettify()

text_file = open("Soup1.txt", "w")
text_file.write(soup1.prettify())
text_file.close()

web_data=soup1
web_data_moded=web_data

pool_name='font-medium text-lg mb-2 undefined'
liqu='mt-2.5 text-xl font-medium text-default'
fixed='bg-white shadow-lg pt-3 px-6 pb-6 rounded-lg py-4 mt-4 items-center pr-2 shadow'
#re.sub('bg-white shadow-lg pt-3 px-6 pb-6 rounded-lg py-4 mt-4 items-center pr-2 shadow(.*?)>', fixed, web_data_moded)
remlist=re.findall('bg-white shadow-lg pt-3 px-6 pb-6 rounded-lg py-4 mt-4 items-center pr-2 shadow(.*?)>', str(web_data_moded))

web_data_moded2=web_data_moded
for i in remlist:
  web_data_moded2=str(web_data_moded2).replace(i,'"')
web_data_mod=BeautifulSoup(web_data_moded2)
main_list=web_data_mod.find_all( "div" , class_=fixed)

main_dict=[]
for i in main_list:
  record=[]
  record.append(i.find( "div" , class_=pool_name ).contents[0])
  record.append(i.find_all( "div" , class_=liqu )[0].contents[0])
  record.append(i.find_all( "div" , class_=liqu )[1].contents[0])
  main_dict.append(record) 
df = pd.DataFrame(main_dict, columns = ['Pool', 'Total Liquidity','APR'])
df.to_csv('Nerve_Fi.csv')
print(df)
#files.download('Nerve_Fi.csv')



"""#### Sushi Farm"""

chrome_options.add_argument('--no-sandbox') 
chrome_options.add_argument('--disable-dev-shm-usage')

url = "https://app.sushi.com/farm"
SCROLL_PAUSE_TIME = 3
#driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
driver = webdriver.Chrome(executable_path=os.getenv('CHROME_EXECUTABLE_PATH'), options=chrome_options)
driver.get(url)

'''
def reload_driver(driver):
  driver.close()
  driver.quit()
  driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
  driver.get(url)
  chrome_options = webdriver.ChromeOptions() 
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
'''

time.sleep(10)



#last_height = driver.execute_script("return document.body.scrollHeight")
last_height= 0
'''
try:
  last_height = driver.execute_script("return document.body.scrollHeight")
except:
  reload_driver(driver)
'''


while True:

  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

  time.sleep(SCROLL_PAUSE_TIME)

  new_height = driver.execute_script("return document.body.scrollHeight")
  if new_height == last_height:
      break
  last_height = new_height
  print(last_height)
page2 = driver.execute_script('return document.body.innerHTML')
soup2 = BeautifulSoup(''.join(page2), 'html.parser')

text_file = open("Soup2.txt", "w")
text_file.write(soup2.prettify())
text_file.close()
#files.download('Soup2.txt')

web_data_sushi=soup2
one_rec='w-full px-4 py-6 text-left rounded cursor-pointer select-none bg-dark-900 text-primary text-sm md:text-lg'
apr_div='flex flex-row items-center font-bold text-right text-high-emphesis'
TVL_div='flex flex-col justify-center font-bold'
pool_sushi= 'flex flex-col justify-center'

main_list_sushi = web_data_sushi.find_all( "button" , class_=one_rec)

import pandas as pd

main_dict=[]
for i in main_list_sushi:
  record=[]
  lsi=i.find( "div" , class_=pool_sushi ).contents[0]
  record.append(lsi.contents[0].contents[0]+lsi.contents[1]+lsi.contents[2].contents[0])
  record.append(i.find( "div" , class_=TVL_div ).contents[0])
  record.append(i.find( "div" , class_=apr_div ).contents[0])
  main_dict.append(record) 
df = pd.DataFrame(main_dict, columns = ['Pool', 'TVL','APR'])
df.to_csv('SushiFarm.csv')
print(df)
#files.download('SushiFarm.csv')

"""#### Adamant"""

url = "https://adamant.finance/"

#driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
driver = webdriver.Chrome(executable_path=os.getenv('CHROME_EXECUTABLE_PATH'), options=chrome_options)
driver.get(url)
SCROLL_PAUSE_TIME = 3

time.sleep(10)

last_height = driver.execute_script("return document.body.scrollHeight")

driver.get_cookies()
import time
while True:

  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

  time.sleep(SCROLL_PAUSE_TIME)

  new_height = driver.execute_script("return document.body.scrollHeight")
  if new_height == last_height:
      break
  last_height = new_height
  print(last_height)
page3 = driver.execute_script('return document.body.innerHTML')
soup3 = BeautifulSoup(''.join(page3), 'html.parser')

text_file = open("Soup3.txt", "w")
text_file.write(soup3.prettify())
text_file.close()

web_data_adm=soup3

one_rec='farms-card-item highlight no-select clickable collapsed'
one_rec2='farms-card-item no-select clickable collapsed'
apr_div='rates'
TVL_div='details total'
pool_ada= 'farms-card-item highlight no-select clickable expanded'

main_list_adm1 = web_data_adm.find_all( "div" , class_=one_rec2)
main_list_adm2 = web_data_adm.find_all( "div" , class_=one_rec)
main_list_adm=main_list_adm1+main_list_adm2
type(main_list_adm)

main_list_adm[0].find( "div" , class_=pool_ada )

import pandas as pd

main_dict=[]
for i in main_list_adm:
  record=[]
  record.append(i.find( "div" , class_='label' ).contents[0].contents[0])
  #record.append(i.find( "div" , class_=TVL_div ).contents[1].contents[0])
  record.append(i.find( "div" , class_=TVL_div ).find( "span" , class_='value' ).contents[0])
  record.append(i.find( "div" , class_=apr_div ).find( "span" , class_='apy' ).contents[0])
  main_dict.append(record) 
df = pd.DataFrame(main_dict, columns = ['Pool', 'TVL','APR'])

df.to_excel('Adament.xlsx')
print(df)
#files.download('Adament.xlsx')
