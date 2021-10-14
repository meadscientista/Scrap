from selenium import webdriver
import bs4
import requests
from bs4 import BeautifulSoup
import pandas as pd
from google.colab import files
from zipfile import ZipFile
import warnings
import re
import pandas as pd
from datetime import date
from datetime import datetime
import time
warnings.filterwarnings("ignore", category=DeprecationWarning)


from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions() 
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

"""##### Declarations"""

global nerve_fail
global sushi_fail
global adm_fail
nerve_fail=0
sushi_fail=0
adm_fail=0
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
  chrome_options = webdriver.ChromeOptions() 
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)





"""##### Definitions"""

def nerve_fi():
  print("Started Nerve Fi")
  url = "https://nerve.fi/pools"
  global nerve_fail
  try:
    print("Running")
    SCROLL_PAUSE_TIME = 3
    driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
    driver.get(url)
    time.sleep(10)
    
    WebDriverWait(driver, SCROLL_PAUSE_TIME)
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:

      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

      time.sleep(SCROLL_PAUSE_TIME)

      new_height = driver.execute_script("return document.body.scrollHeight")
      if new_height == last_height:
          break
      last_height = new_height
    page1 = driver.execute_script('return document.body.innerHTML')
    soup1 = BeautifulSoup(''.join(page1), 'html.parser')

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
    df = pd.DataFrame(main_dict, columns = ['Pool', 'TVL','APR'])
    df.to_csv('Nerve_Fi.csv')
    print("Extracted in ",nerve_fail+1,"attempts")
    print("Extracted ",len(df)," records")

  except:
    nerve_fail=nerve_fail+1
    print('Failed ',nerve_fail,' times')
    try:
      initialize()
    except:
      pass
    if nerve_fail<4:
      nerve_fi()
    else:
      print('Error in Nerve.Fi')
      exit()

      


  return df

def sushi_farm():
  url = "https://app.sushi.com/farm"
  SCROLL_PAUSE_TIME = 3
  global sushi_fail
  print('Started Sushi')
   
  try:
    print('Running Sushi')
    driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
    driver.get(url)

    time.sleep(10)
    last_height = driver.execute_script("return document.body.scrollHeight")
    #last_height= 0

    while True:

      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

      time.sleep(SCROLL_PAUSE_TIME)

      new_height = driver.execute_script("return document.body.scrollHeight")
      #print(new_height)
      if new_height == last_height:
          break
      last_height = new_height
    page2 = driver.execute_script('return document.body.innerHTML')
    soup2 = BeautifulSoup(''.join(page2), 'html.parser')

    text_file = open("Soup2.txt", "w")
    text_file.write(soup2.prettify())
    text_file.close()

    web_data_sushi=soup2
    one_rec='w-full px-4 py-6 text-left rounded cursor-pointer select-none bg-dark-900 text-primary text-sm md:text-lg'
    apr_div='flex flex-row items-center font-bold text-right text-high-emphesis'
    TVL_div='flex flex-col justify-center font-bold'
    pool_sushi= 'flex flex-col justify-center'

    main_list_sushi = web_data_sushi.find_all( "button" , class_=one_rec)

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
    print("Extracted in ",sushi_fail+1,"attempts")
    print("Extracted ",len(df)," records")
    return df
  except:

    sushi_fail=sushi_fail+1
    print('Failed ',sushi_fail,' times')
    try:
      initialize()

    except:
      pass

    if sushi_fail<5:
      sushi_farm()
    else:
      print('Error in Sushi Farm')
      exit()
  return df

def adamant():
  print("Started Adamant")
  url = "https://adamant.finance/"
  import time
  global adm_fail
  try:    
    driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
    driver.get(url)
    SCROLL_PAUSE_TIME = 3

    time.sleep(10)

    last_height = driver.execute_script("return document.body.scrollHeight")

    driver.get_cookies()
    while True:

      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

      time.sleep(SCROLL_PAUSE_TIME)

      new_height = driver.execute_script("return document.body.scrollHeight")
      if new_height == last_height:
          break
      last_height = new_height
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
    main_list_adm[0].find( "div" , class_=pool_ada )
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
    return df
    print("Extracted in ",adm_fail+1,"attempts")
    

  except:
    adm_fail=adm_fail+1
    print('Failed ',adm_fail,' times')
    try:
      initialize()
      
    except:
      pass
    if adm_fail<4:
      adamant()
    else:
      print('Error in Adamant')
      exit()

      


  return df

def All_Crypto():
  All_websites = pd.DataFrame(columns = ['Pool', 'TVL','APR','source'])

  try:
    print('Nerve Try 1')
    op=nerve_fi()
    Nerve_File='Nerve Fi '+date_time_now+'.xlsx'
    op.to_excel(Nerve_File)
    Nerve_df=op.assign(source='Nerve.fi')
    All_websites=All_websites.append(Nerve_df)
    print(Nerve_df)
    
  except:
    try:
      initialize()
    except:
      try:
        print('Nerve Try 2')
        op=nerve_fi()
        Nerve_File='Nerve Fi '+date_time_now+'.xlsx'
        op.to_excel(Nerve_File)
        Nerve_df=op.assign(source='Nerve.fi')
        All_websites=All_websites.append(Nerve_df)
      except:
        print('Failed to Extract Nerve.Fi')

  try:
    print('Sushi Try 1')
    op2=sushi_farm()
    print('Extracted Sushi ')
    Sushi_File='Sushi Farm '+date_time_now+'.xlsx'
    op2.to_excel(Sushi_File)
    Sushi_df=op2.assign(source='Sushi')
    print('Appended Sushi ')
    All_websites=All_websites.append(Sushi_df)
    print(Sushi_df)

  except:
    try:
      initialize()
    except:
      try:
        print('Sushi Try 2')
        op2=sushi_farm()
        Sushi_File='Sushi Farm '+date_time_now+'.xlsx'
        op2.to_excel(Sushi_File)
        Sushi_df=op2.assign(source='Sushi Farm')
        All_websites=All_websites.append(Sushi_df)
        print(Sushi_df)
      except:
        print('Failed to Extract Sushi Farm')
  
  
  
  try:
    print('Adamant Try 1')
    op3=adamant()
    Adm_File='Adamant '+date_time_now+'.xlsx'
    op3.to_excel(Adm_File)
    Adamant_df=op3.assign(source='Adamant')
    All_websites=All_websites.append(Adamant_df)
    print(Adamant_df)
  except:
    try:
      initialize()
    except:
      try:
        print('Adamant Try 2')
        op3=adamant()
        Adm_File='Adamant '+date_time_now+'.xlsx'
        op3.to_excel(Adm_File)
        Adamant_df=op3.assign(source='Adamant')
        All_websites=All_websites.append(Adamant_df)
        print(Adamant_df)
      except:
        print('Failed to Extract Adamant')
  
  return All_websites

"""### Execution"""

All_Websites_df=All_Crypto()
Full_Data='Full Crypto '+date_time_now+'.xlsx'

All_Websites_df.to_excel(Full_Data)
All_Websites_df
