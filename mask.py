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
EXTENSION_PATH = 'mask.crx'
chrome_options.add_argument(EXTENSION_PATH)

#driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
driver = webdriver.Chrome(executable_path=os.getenv('CHROME_EXECUTABLE_PATH'), options=chrome_options)


from selenium import webdriver
print('1')
EXTENSION_PATH = 'mask.crx'
print('2')
#opt = webdriver.ChromeOptions()
print('3')
#opt.add_extension(EXTENSION_PATH)
print('4')
#driver = webdriver.Chrome(chrome_options=opt)
print('5')
time.sleep(10)
print('6')
#driver.maximize_window()
'''
try:
    driver.switch_to.window(driver.window_handles[-1])
    print('___________________________________________________________________')
    print('Switch 1___________________________________________________________________')
    page1 = driver.execute_script('return document.body.innerHTML')
    soup1 = BeautifulSoup(''.join(page1), 'html.parser')
    print(soup1.prettify())

except:
    pass
try:
    driver.switch_to.window(driver.window_handles[0])
    print('___________________________________________________________________')
    print('Switch 2___________________________________________________________________')
    page1 = driver.execute_script('return document.body.innerHTML')
    soup1 = BeautifulSoup(''.join(page1), 'html.parser')
    print(soup1.prettify())    
except:
    pass
try:
    driver.switch_to.window(driver.window_handles[1])
    print('___________________________________________________________________')
    print('Switch 3___________________________________________________________________')
    page1 = driver.execute_script('return document.body.innerHTML')
    soup1 = BeautifulSoup(''.join(page1), 'html.parser')
    print(soup1.prettify())    

    print('___________________________________________________________________')
    
except:
    pass
'''
print('Window Switched')
length=len(driver.window_handles)
titles=[]
for i in range(length):
    driver.switch_to.window(driver.window_handles[i])
    titles.append(driver.title)
    print(title)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
try:
    driver.find_element_by_xpath('//button[text()="Get Started"]').click()
    driver.find_element_by_xpath('//button[text()="Import wallet"]').click()
    driver.find_element_by_xpath('//button[text()="No Thanks"]').click()
except:
    print('Failed 0')
    pass

time.sleep(2)
inputs = driver.find_elements_by_xpath('//input')

try:
    inputs[0].send_keys('model modify hand end attack dove resource find delay because smile plastic')
    inputs[1].send_keys('Scraper@2021')
    inputs[2].send_keys('Scraper@2021')
except:
    print('Failed 1')
    pass
time.sleep(2)
try:    
    driver.find_element_by_css_selector('.first-time-flow__checkbox.first-time-flow__terms').click()
    #first-time-flow__checkbox first-time-flow__terms
    #driver.find_element_by_xpath('//div[class="first-time-flow__checkbox first-time-flow__terms"]').click()
    driver.find_element_by_xpath('//button[text()="Import"]').click()
except:
    print('Failed 2')
    pass
time.sleep(5)
try:
    driver.find_element_by_xpath('//button[text()="All Done"]').click()
except:
    print('Failed 3')
    pass

page1 = driver.execute_script('return document.body.innerHTML')
soup1 = BeautifulSoup(''.join(page1), 'html.parser')
print(soup1.prettify())
