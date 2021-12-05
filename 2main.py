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
from pytz import timezone
import pytz
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
global coingecko_fail
global pangolin_fail
global alpaca_fail

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
coingecko_fail=0
pangolin_fail=0
alpaca_fail=0

date_time_now=str(datetime.now(pytz.timezone('Hongkong')))[:16]



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

TOKEN = "D9kbx5Cwjw0AAAAAAAAAAa7JeHpbCvlVs60FIOmrNFRRQ5_CjsoHqQ5QMJV0VrIr"


def connect_to_dropbox():
  try:
    dbx = dropbox.Dropbox(TOKEN)
    print('Connected to Dropbox successfully')
    return dbx
  except Exception as e:
    print(str(e))
  #return dbx


  
def upload_file(file_from, file_to):
    dbx = dropbox.Dropbox(TOKEN)
    f = open(file_from, 'rb')
    dbx.files_upload(f.read(), file_to)
    
def Failure_Email(Missing):
  gmail_user = 'cryptopoolscrap@gmail.com'
  gmail_password = 'scraper@2021'

  sent_from = gmail_user
  to = ['meadscientista@gmail.com','pandeyos@rknec.edu']
  subject = 'Crypto Pool : Failure Alert'
  fail=''
  for i in Missing:
    fail=fail+'Data from '+i+' source is missing.\n\n'
    
  body = fail + "Please check website and source file to ensure allignment. If the file isn't alligned with website, trigger a mannual run to get the updated data from website."
  try:
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security   
    s.starttls()
    # Authentication  
    s.login(gmail_user, gmail_password)
    # message to be sent   
    SUBJECT = subject   
    TEXT = body
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    # sending the mail    
    s.sendmail(sent_from, to, message)
    # terminating the session    
    s.quit()
    print('Email Sent')
  except Exception as ex:
    print ("Something went wrong….",ex)


"""##### Definitions

###### Old
"""

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

"""###### New"""

def mirror():
  print("Started Mirror")
  url = "https://mirrorprotocol.app/#/farm"
  import time
  global mirror_fail
  try:    
    driver=webdriver.Chrome(executable_path=os.getenv('CHROME_EXECUTABLE_PATH'), options=chrome_options)
    driver.get(url)
    SCROLL_PAUSE_TIME = 3

    time.sleep(10)

    last_height = driver.execute_script("return document.body.scrollHeight")
    opname='Mirror'+str(date_time_now)+'.csv'

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
    web_data=soup3

    text_file = open("Soup3.txt", "w")
    text_file.write(soup3.prettify())
    text_file.close()
    main_list=web_data.find_all( "tr")
    main_dict=[]

    for i in main_list:
        record=[]
        roww=i.find_all( "td")
        rows=str(roww)
        #print(i.contents)
        ##record.append(i.find( "h1" , class_='AssetItem_symbol__3_Oq5'))
        ##record.append(i.find_all( "span"))
        start = rows.find('class="AssetItem_symbol__3_Oq5">') + len('class="AssetItem_symbol__3_Oq5">')
        end = rows.find('</h1><')
        record.append(rows[start:end])

        start = rows.find('Table_clickable__2uZdi Table_td__21T1w"><span ') + len('Table_clickable__2uZdi Table_td__21T1w"><span ')
        end = rows.find('<small>%</small></span><p class="FarmList_link__1wHkQ">Long <')
        substrx=rows[start:end]
        record.append(substrx[substrx.find('">')+2:end])
        #print(rows)

        start = rows.find('Table_clickable__2uZdi Table_td__21T1w"><span') + len('Table_clickable__2uZdi Table_td__21T1w"><span')
        end = rows.find('<small>%</small></span><p class="FarmList_link__1wHkQ">Short')
        substrx=rows[start:end]
        start = substrx.find('Table_clickable__2uZdi Table_td__21T1w"><span') + len('Table_clickable__2uZdi Table_td__21T1w"><span')
        substrxx=substrx[start:]
        #start = substrx.find('Table_clickable__2uZdi Table_td__21T1w"><span') + len('Table_clickable__2uZdi Table_td__21T1w"><span')
        #end = substrx.find('<small>%</small></span><p class="FarmList_link__1wHkQ">Short')
        #substrx=rows[start:]
        if(start>0 and end>0):
            record.append(substrxx[substrxx.find('">')+2:end])
        else:
            record.append('')



        start = rows.find('Table_desktop__2eaNS Table_td__21T1w"><span class="">') + len('Table_desktop__2eaNS Table_td__21T1w"><span class="">')
        end = rows.find('<small>%</small></span></td>')
        #print(start,end)
        substrx=rows[start:end]
        if(start>0 and end>0):
            record.append(substrx)
        else:
            record.append('')
        #print(record)

        #record.append(i.find_all( "div" , class_=liqu )[1].contents[0])
        main_dict.append(record) 
        #listmirror=[x for x in i.find_all( "span")]
        #i.find_all( "span")
        #print(roww)

        #print(re.search(r'class="AssetItem_symbol__3_Oq5">(.*?)</h1><', str(roww)))
        #print((i.find_all( "span")))
    df = pd.DataFrame(main_dict, columns = ['Ticker', 'Long','Short','APR'])
    #print("Extracted in ",nerve_fail+1,"attempts")
    #print("Extracted ",len(df)," records")
    df.to_csv(opname)
    file_from = opname  
    file_to = '/'+opname
    upload_file(file_from,file_to)
    
    return df
    print("Extracted in ",mirror_fail+1,"attempts")
    

  except:
    mirror_fail=mirror_fail+1
    print('Failed ',mirror_fail,' times')
    try:
      initialize()
      
    except:
      pass
    if mirror_fail<4:
      mirror()
    else:
      print('Error in Mirror')
      exit()

      


  return df

def convex():
  print("Started Convex")
  url="https://www.convexfinance.com/stake"
  import time
  global convex_fail
  try:
    chrome_options.add_argument('--no-sandbox') 
    chrome_options.add_argument('--disable-dev-shm-usage') 
    driver=webdriver.Chrome(executable_path=os.getenv('CHROME_EXECUTABLE_PATH'), options=chrome_options)
    SCROLL_PAUSE_TIME = 4

    driver.maximize_window()

    WebDriverWait(driver, SCROLL_PAUSE_TIME)
    '''
    driver.get(url)
    time.sleep(timeout)
    content = driver.page_source
    '''



    driver.get(url)
    time.sleep(2)


    last_height = 0

    import time
    while True:

        # Scroll down to bottom
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
      time.sleep(SCROLL_PAUSE_TIME)


        # Calculate new scroll height and compare with last scroll height
      new_height = driver.execute_script("return document.body.scrollHeight")
      if new_height == last_height:
          break
      last_height = new_height

    #element = driver.find_element_by_css_selector(".MuiButtonBase-root.MuiButton-root.MuiButton-outlined.show-all-pools-button.MuiButton-outlinedSizeLarge.MuiButton-sizeLarge")
    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiButtonBase-root.MuiButton-root.MuiButton-outlined.show-all-pools-button.MuiButton-outlinedSizeLarge.MuiButton-sizeLarge"))).click()

    element = driver.find_element_by_xpath("//button[@class='MuiButtonBase-root MuiButton-root MuiButton-outlined show-all-pools-button   MuiButton-outlinedSizeLarge MuiButton-sizeLarge']")

    element.click()
    time.sleep(SCROLL_PAUSE_TIME)
    #optable = str(soup.find( "div" , class_='PaginatedTable__table-full___35BKu' )) 
    #last_height = driver.execute_script("return document.body.scrollHeight")

    last_height = 0

    import time
    while True:

        # Scroll down to bottom
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
      time.sleep(SCROLL_PAUSE_TIME)


        # Calculate new scroll height and compare with last scroll height
      new_height = driver.execute_script("return document.body.scrollHeight")
      if new_height == last_height:
          break
      last_height = new_height

    page1 = driver.execute_script('return document.body.innerHTML')
    soup1 = BeautifulSoup(''.join(page1), 'html.parser')
    web_data=soup1
    main_list=web_data.find_all("div",class_= "jsx-2417581814 container secondary not-always-expanded has-no-nested-action-box ")
    main_dict=[]
    import re
    for i in main_list:
        record=[]
        roww=i
        rowws=str(roww)

        #print(i.contents)
        ##record.append(i.find( "h1" , class_='AssetItem_symbol__3_Oq5'))
        ##record.append(i.find_all( "span"))

        record.append(roww.find('div',class_='jsx-495322019 container').contents[0])
        vapr=str(roww.find_all('span',class_='jsx-3178637786 container ')[1].contents[0])

        record.append(vapr[ vapr.find('<span>') + len('<span>'):vapr.find('<span class')])
        aprr=rowws[ rowws.find('<br/>CRV boost: ') + len('<br/>CRV boost: '):rowws.find('</span></span></div><div class="jsx-3073295382')]
        if(len(str(aprr))<6):
          record.append(aprr)
        else:
          record.append('')
        liq=str(roww.find_all('div',class_='jsx-3073295382 container vertical ')[-1].contents[0])
        liqq=liq[ liq.find('$') + len('$'):vapr.find(']]')]
    
        record.append(liqq[ liqq.find('</span>') + len('</span>'):-6])

        #record.append(i.find_all( "div" , class_=liqu )[1].contents[0])
        main_dict.append(record) 
        #listmirror=[x for x in i.find_all( "span")]
        #i.find_all( "span")
        #print(roww)

        #print(re.search(r'class="AssetItem_symbol__3_Oq5">(.*?)</h1><', str(roww)))
        #print((i.find_all( "span")))
    df = pd.DataFrame(main_dict, columns = ['Pool Name', 'Vapr','CVR Boost','TVL'])
    #print("Extracted in ",nerve_fail+1,"attempts")
    #print("Extracted ",len(df)," records")
    df.to_csv('Convex.csv')

    return df
    print("Extracted in ",convex_fail+1,"attempts")
    

  except:
    convex_fail=convex_fail+1
    print('Failed ',convex_fail,' times')
    try:
      initialize()
      
    except:
      pass
    if convex_fail<4:
      convex()
    else:
      print('Error in Convex')
      exit()

      


  return df

def raydium():
  print("Started Raydium")
  url="https://raydium.io/farms/"
  import time
  global raydium_fail
  chrome_options.add_argument("--start-maximized")
  try:

    driver=webdriver.Chrome(executable_path=os.getenv('CHROME_EXECUTABLE_PATH'), options=chrome_options)

    SCROLL_PAUSE_TIME = 4
    driver.set_window_size(1024, 600)
    driver.maximize_window()
    WebDriverWait(driver, SCROLL_PAUSE_TIME)
    driver.get(url)
    time.sleep(2)
    last_height = 0
    while True:

        # Scroll down to bottom
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
      time.sleep(SCROLL_PAUSE_TIME)


        # Calculate new scroll height and compare with last scroll height
      new_height = driver.execute_script("return document.body.scrollHeight")
      if new_height == last_height:
          break
      last_height = new_height

    #element = driver.find_element_by_css_selector(".MuiButtonBase-root.MuiButton-root.MuiButton-outlined.show-all-pools-button.MuiButton-outlinedSizeLarge.MuiButton-sizeLarge")
    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiButtonBase-root.MuiButton-root.MuiButton-outlined.show-all-pools-button.MuiButton-outlinedSizeLarge.MuiButton-sizeLarge"))).click()
    time.sleep(8)
    #optable = str(soup.find( "div" , class_='PaginatedTable__table-full___35BKu' )) 
    #last_height = driver.execute_script("return document.body.scrollHeight")

    last_height = 0

    import time
    while True:

        # Scroll down to bottom
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
      time.sleep(SCROLL_PAUSE_TIME)


        # Calculate new scroll height and compare with last scroll height
      new_height = driver.execute_script("return document.body.scrollHeight")
      if new_height == last_height:
          break
      last_height = new_height

    page1 = driver.execute_script('return document.body.innerHTML')
    soup1 = BeautifulSoup(''.join(page1), 'html.parser')    #print("Extracted in ",nerve_fail+1,"attempts")
    web_data=BeautifulSoup(str(soup1).replace('<!-- --> <div data-v-6ec849c0="">',''))
    main_list=web_data.find_all("div",class_= "ant-collapse-item")
    main_dict=[]
    import re
    for i in main_list:
        record=[]
        roww=i
        rowws=str(roww)

        #print(i.contents)
        ##record.append(i.find( "h1" , class_='AssetItem_symbol__3_Oq5'))
        ##record.append(i.find_all( "span"))

        record.append(roww.find('div',class_='lp-icons ant-col ant-col-8').contents[1].strip())
        #vapr=str(roww.find_all('span',class_='jsx-3178637786 container ')[1].contents[0])
        #print(roww.find('div',class_='state ant-col ant-col-6').find('div',class_='value'))
        
        aprr=str(roww.find_all('div',class_='value')[1].contents[0])
        aprs=aprr[ aprr.find('c0="">') + len('c0="">'):aprr.find('</div>')].strip().replace("\n", '')
        
        
        record.append(aprs)
        #liq=str(roww.find_all('div',class_='jsx-3073295382 container vertical ')[-1].contents[0])
        #liqq=liq[ liq.find('$') + len('$'):vapr.find(']]')]
    
        record.append(str(roww.find('div',class_='state ant-col ant-col-6').find('div',class_='value').contents[0].strip().replace("\n", '')))

        #record.append(i.find_all( "div" , class_=liqu )[1].contents[0])
        main_dict.append(record) 
        #listmirror=[x for x in i.find_all( "span")]
        #i.find_all( "span")
        #print(roww)

        #print(re.search(r'class="AssetItem_symbol__3_Oq5">(.*?)</h1><', str(roww)))
        #print((i.find_all( "span")))
    df = pd.DataFrame(main_dict, columns = ['Pool Name','APR','TVL'])
    #print("Extracted in ",nerve_fail+1,"attempts")
    #print("Extracted ",len(df)," records")
    df.to_csv('Raydium.csv')
    return df
    print("Extracted in ",raydium_fail+1,"attempts")
    

  except:
    raydium_fail=raydium_fail+1
    print('Failed ',raydium_fail,' times')
    try:
      initialize()
      
    except:
      pass
    if raydium_fail<4:
      raydium()
    else:
      print('Error in Raydium')
      exit()

      


  return df

def balancer():
  print("Started Balancer")
  url="https://polygon.balancer.fi/#/"
  import time
  global balancer_fail
  chrome_options.add_argument("--start-maximized")
  try:
    
    chrome_options.add_argument('--no-sandbox') 
    chrome_options.add_argument('--disable-dev-shm-usage') 
    driver=webdriver.Chrome(executable_path=os.getenv('CHROME_EXECUTABLE_PATH'), options=chrome_options)

    SCROLL_PAUSE_TIME = 4
    driver.set_window_size(1024, 600)
    driver.maximize_window()
    WebDriverWait(driver, SCROLL_PAUSE_TIME)
    driver.get(url)
    time.sleep(2)
    last_height = 0
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    try:
        #print('In')
        #element = driver.find_element_by_xpath("//div[@class='bal-icon inline-block ml-2']")
        time.sleep(SCROLL_PAUSE_TIME)
        element = driver.find_element_by_xpath("//div[@class='bal-table-pagination-btn']")    
        element.click()
        time.sleep(3)    
        #print('click_a')
    except:
        #print('failed')
        pass

    while True:
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
      time.sleep(SCROLL_PAUSE_TIME)
      try:
        #element = driver.find_element_by_xpath("//div[@class='bal-icon inline-block ml-2']")
        time.sleep(SCROLL_PAUSE_TIME)
        element = driver.find_element_by_xpath("//div[@class='bal-table-pagination-btn']")    
        element.click()
        time.sleep(SCROLL_PAUSE_TIME)
        #print('click')
        #print(new_height,last_height)

      except:
        
        #print('failed')
        pass


        # Calculate new scroll height and compare with last scroll height
      new_height = driver.execute_script("return document.body.scrollHeight")
      if new_height == last_height:
          break
      last_height = new_height

      #print(new_height,last_height)

    page1 = driver.execute_script('return document.body.innerHTML')
    soup1 = BeautifulSoup(''.join(page1), 'html.parser')

    web_data=soup1
    main_list=web_data.find_all("tr",class_= "bg-white z-10 row-bg group cursor-pointer")
    main_dict=[]
    import re
    for i in main_list:
        record=[]
        roww=i
        rowws=str(roww)

        #print(i.contents)
        ##record.append(i.find( "h1" , class_='AssetItem_symbol__3_Oq5'))
        ##record.append(i.find_all( "span"))
        Comp=[]
        for i in roww.find('div',class_='px-6 py-4 flex items-center').contents[0].contents:
            try:
                Comp.append(i.contents[1].contents[0])
            except:
                pass    
        #composition=[i.contents[1].contents[0] for i in roww.find('div',class_='px-6 py-4 flex items-center').contents[0].contents]

        record.append(Comp)

        #aprr=str(roww.find_all('div',class_='value')[1].contents[0])
        #aprs=aprr[ aprr.find('c0="">') + len('c0="">'):aprr.find('</div>')].strip().replace("\n", '')
        
        
        record.append(roww.find('div',class_='px-6 py-4 text-right font-numeric').contents[0])
        #liq=str(roww.find_all('div',class_='jsx-3073295382 container vertical ')[-1].contents[0])
        #liqq=liq[ liq.find('$') + len('$'):vapr.find(']]')]
    
        record.append(roww.find('div',class_='px-6 py-4 -mt-1 flex justify-end font-numeric').contents[0])

        #record.append(i.find_all( "div" , class_=liqu )[1].contents[0])
        main_dict.append(record) 
        #listmirror=[x for x in i.find_all( "span")]
        #i.find_all( "span")
        #print(roww)

        #print(re.search(r'class="AssetItem_symbol__3_Oq5">(.*?)</h1><', str(roww)))
        #print((i.find_all( "span")))
    df = pd.DataFrame(main_dict, columns = ['Composition','Pool Value','APR'])
    #print("Extracted in ",nerve_fail+1,"attempts")
    #print("Extracted ",len(df)," records")
    df.to_csv('Balancer.csv')



    return df
    print("Extracted in ",raydium_fail+1,"attempts")
    

  except:
    balancer_fail=balancer_fail+1
    print('Failed ',balancer_fail,' times')
    try:
      initialize()
      
    except:
      pass
    if balancer_fail<4:
      balancer()
    else:
      print('Error in Balancer')
      exit()

      


  return df

def ubeswap():
  print("Started Ubeswap")
  url="https://app.ubeswap.org/#/farm"
  import time
  global ubeswap_fail
  chrome_options.add_argument("--start-maximized")
  try:
       
    chrome_options.add_argument('--no-sandbox') 
    chrome_options.add_argument('--disable-dev-shm-usage') 
    driver=webdriver.Chrome(executable_path=os.getenv('CHROME_EXECUTABLE_PATH'), options=chrome_options)

    SCROLL_PAUSE_TIME = 3


    WebDriverWait(driver, SCROLL_PAUSE_TIME)
    '''
    driver.get(url)
    time.sleep(timeout)
    content = driver.page_source
    '''

    driver.get(url)
    time.sleep(SCROLL_PAUSE_TIME)

    #optable = str(soup.find( "div" , class_='PaginatedTable__table-full___35BKu' )) 
    #last_height = driver.execute_script("return document.body.scrollHeight")


    page1 = driver.execute_script('return document.body.innerHTML')
    soup1 = BeautifulSoup(''.join(page1), 'html.parser')

    web_data=soup1

    main_list=web_data.find_all( "div" , class_='sc-gqdwHF cDPyLo')
    main_dict=[]
    for i in main_list:
        roww=i
        record=[]
        record.append(roww.find('div',class_='sc-cxFLGX cNbTaJ css-1t1fovp').contents[0])
        record.append(roww.find_all('div',class_='sc-cxFLGX cNbTaJ css-8626y4')[2].contents[0])
        record.append(roww.find('div',class_='sc-cxFLGX gDnfWa apr css-zhpkf8').contents[0])

        main_dict.append(record) 
    df = pd.DataFrame(main_dict, columns = ['Pool', 'TVL','APR'])
    #print("Extracted in ",nerve_fail+1,"attempts")
    print("Extracted ",len(df)," records")
    df.to_csv('Ubeswap.csv')


    return df
    print("Extracted in ",ubeswap_fail+1,"attempts")
    

  except:
    ubeswap_fail=ubeswap_fail+1
    print('Failed ',ubeswap_fail,' times')
    try:
      initialize()
      
    except:
      pass
    if ubeswap_fail<4:
      ubeswap()
    else:
      print('Error in Ubeswap')
      exit()

      


  return df

def bybit():
  print("Started bybit")
  url="https://www.bybit.com/trade/usdt/BITUSDT"
  import time
  global bybit_fail
  chrome_options.add_argument("--start-maximized")
  try:
       
    chrome_options.add_argument('--no-sandbox') 
    chrome_options.add_argument('--disable-dev-shm-usage') 
    driver=webdriver.Chrome(executable_path=os.getenv('CHROME_EXECUTABLE_PATH'), options=chrome_options)

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

def pancake():
  print("Started pancake")
  url="https://pancakeswap.finance/farms"
  import time
  global pancake_fail
  chrome_options.add_argument("--start-maximized")
  try:

       
    chrome_options.add_argument('--no-sandbox') 
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--start maximised')  
    driver=webdriver.Chrome(executable_path=os.getenv('CHROME_EXECUTABLE_PATH'), options=chrome_options)
    driver.set_window_size(2048, 1200)
    driver.maximize_window()
    SCROLL_PAUSE_TIME = 4

    driver.maximize_window()

    WebDriverWait(driver, SCROLL_PAUSE_TIME)
    '''
    driver.get(url)
    time.sleep(timeout)
    content = driver.page_source
    '''



    driver.get(url)
    time.sleep(2)


    last_height = 0

    import time
    while True:
      time.sleep(SCROLL_PAUSE_TIME)
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight-1000);")
      #driver.execute_script("scrollBy(0,250);")
      time.sleep(SCROLL_PAUSE_TIME)
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight-600);")
        # Wait to load page
      #time.sleep(SCROLL_PAUSE_TIME)
      new_height = driver.execute_script("return document.body.scrollHeight")
      if new_height == last_height:
          break
      last_height = new_height

    #element = driver.find_element_by_css_selector(".MuiButtonBase-root.MuiButton-root.MuiButton-outlined.show-all-pools-button.MuiButton-outlinedSizeLarge.MuiButton-sizeLarge")
    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiButtonBase-root.MuiButton-root.MuiButton-outlined.show-all-pools-button.MuiButton-outlinedSizeLarge.MuiButton-sizeLarge"))).click()

    time.sleep(SCROLL_PAUSE_TIME)
    #optable = str(soup.find( "div" , class_='PaginatedTable__table-full___35BKu' )) 
    #last_height = driver.execute_script("return document.body.scrollHeight")


    page1 = driver.execute_script('return document.body.innerHTML')
    soup1 = BeautifulSoup(''.join(page1), 'html.parser') 

    web_data=soup1
    main_list=web_data.find_all("tr",class_= "sc-feWZte jehVgy")
    main_dict=[]
    import re
    for i in main_list:
        record=[]
        roww=i
        rowws=str(roww)

        #print(i.contents)
        ##record.append(i.find( "h1" , class_='AssetItem_symbol__3_Oq5'))
        ##record.append(i.find_all( "span"))

        record.append(roww.find('div',class_='sc-gtsrHT jDnmwq').contents[0])
        
        record.append(roww.find('div',class_='sc-jSFjdj sc-gKAaRy sc-cdlubJ kJmatq togOu kMsWyy').contents[0])
        record.append(roww.find('div',class_='sc-gtsrHT MlLjM').contents[0])
        
        record.append(roww.find('div',class_='sc-hDrgck bgSbZP').contents[0])

        #record.append(i.find_all( "div" , class_=liqu )[1].contents[0])
        main_dict.append(record) 
        #listmirror=[x for x in i.find_all( "span")]
        #i.find_all( "span")
        #print(roww)

        #print(re.search(r'class="AssetItem_symbol__3_Oq5">(.*?)</h1><', str(roww)))
        #print((i.find_all( "span")))
    df = pd.DataFrame(main_dict, columns = ['Pool Name', 'APR','Liquidity','Boost'])
    #print("Extracted in ",nerve_fail+1,"attempts")
    #print("Extracted ",len(df)," records")

    print("Extracted ",pancake_fail+1," records")
    df.to_csv('pancake.csv')
    print(soup1)
    return df
    print("Extracted in ",pancake_fail+1,"attempts")
    

  except:
    pancake_fail=pancake_fail+1
    print('Failed ',pancake_fail,' times')
    try:
      initialize()
      
    except:
      pass
    if pancake_fail<4:
      pancake()
    else:
      print('Error in pancake')
      exit()

      


  return df

def traderjoe():
  print("Started TraderJoe")
  url="https://traderjoexyz.com/#/farm"
  import time
  global traderjoe_fail
  
  try:
    #chrome_options = webdriver.ChromeOptions() 
    chrome_options.add_argument("--start-maximized")
    main_dict=[]
    chrome_options.add_argument('--no-sandbox') 
    chrome_options.add_argument('--disable-dev-shm-usage') 
    driver=webdriver.Chrome(executable_path=os.getenv('CHROME_EXECUTABLE_PATH'), options=chrome_options)
    SCROLL_PAUSE_TIME = 2
    driver.maximize_window()
    WebDriverWait(driver, SCROLL_PAUSE_TIME)
    driver.get(url)
    time.sleep(2)
    last_height = 0
    import time
    for i in range(1,8):
      time.sleep(SCROLL_PAUSE_TIME)
      try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight-1000);")
            time.sleep(SCROLL_PAUSE_TIME)
            gts="//button[@aria-label='Go to page "+str(i)+"']"
            element = driver.find_element_by_xpath(gts) 
            element.click()
            print('click')
      except:
        pass
      page1 = driver.execute_script('return document.body.innerHTML')
      soup1 = BeautifulSoup(''.join(page1), 'html.parser')
      web_data=soup1
      main_list=web_data.find_all("div",class_= "sc-jdeSqf hDGfIi")
      #print(main_list)
      for i in main_list:
        record=[]
        roww=i
        rowws=str(roww)
        record.append(roww.find('div',class_='sc-bZQynM jmMmRU css-r99fas').contents[0]) 
        #print(roww)
        record.append(roww.find_all('div',class_='sc-bZQynM dkmKkO css-1ecm0so')[0].contents[0])
        record.append(roww.find_all('div',class_='sc-bZQynM dkmKkO css-1ecm0so')[1].contents[0])   
        record.append(roww.find_all('div',class_='sc-bZQynM dkmKkO css-1ecm0so')[2].contents[0])
        main_dict.append(record) 
        

    df = pd.DataFrame(main_dict, columns = ['Pool Name', 'Pool Weight','Liquidity','APR'])
    df=df.drop_duplicates(subset=['Pool Name'])
    df.to_csv('Trader Joe.csv')

    print("Extracted ",traderjoe_fail+1," records")
    df.to_csv('traderjoe.csv')
    print(soup1)
    return df
    print("Extracted in ",traderjoe_fail+1,"attempts")
    

  except:
    traderjoe_fail=traderjoe_fail+1
    print('Failed ',traderjoe_fail,' times')
    try:
      initialize()
      
    except:
      pass
    if traderjoe_fail<4:
      traderjoe()
    else:
      print('Error in TraderJoe')
      exit()

      


  return df

def coingecko():
  print("Started Coingecko")
  url="https://www.coingecko.com/en/coins/bitdao#markets"
  import time
  global coingecko_fail
  
  try:
    
    #chrome_options = webdriver.ChromeOptions() 
    main_dict=[]
    chrome_options.add_argument('--no-sandbox') 
    chrome_options.add_argument('--disable-dev-shm-usage') 
    driver=webdriver.Chrome(executable_path=os.getenv('CHROME_EXECUTABLE_PATH'), options=chrome_options)
    SCROLL_PAUSE_TIME = 2
    driver.maximize_window()
    WebDriverWait(driver, SCROLL_PAUSE_TIME)
    driver.get(url)
    time.sleep(2)
    last_height = 0    


    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight-1000);")
        time.sleep(SCROLL_PAUSE_TIME)
        #="coin-tickers-tab.perpetualsButton"
        gts="//div[@data-target='coin-tickers-tab.perpetualsButton']"
        element = driver.find_element_by_xpath(gts) 
        element.click()
        print('click')
    except:
        pass

    page1 = driver.execute_script('return document.body.innerHTML')
    soup1 = BeautifulSoup(''.join(page1), 'html.parser')
    web_data=soup1
    main_list=web_data.find('div',class_='contract-table').find_all("tr")[1:]
    #print(main_list)
    for i in main_list:
        record=[]
        roww=i
        rowws=str(roww)
        record.append(roww.contents[1].contents[3].contents[0]) 
        #print(roww)
        record.append(roww.contents[3].contents[1].contents[0])
        record.append(roww.contents[5].contents[0].strip())   
        record.append(roww.contents[11].contents[0].strip())
        record.append(roww.contents[15].contents[1].contents[0].strip())
        
        
        main_dict.append(record) 


    df = pd.DataFrame(main_dict, columns = ['Exchange', 'Symbol','Price','Basis','Funding Rate'])

    df.to_csv('CoinGecko.csv')

    print("Extracted ",coingecko_fail+1," records")


    return df
    print("Extracted in ",coingecko_fail+1,"attempts")
    

  except:
    coingecko_fail=coingecko_fail+1
    print('Failed ',coingecko_fail,' times')
    try:
      initialize()
      
    except:
      pass
    if coingecko_fail<4:
      coingecko()
    else:
      print('Error in Coingecko')
      exit()

      


  return df

def sushi_nokashi_farm():
  url = "https://app.sushi.com/farm"
  SCROLL_PAUSE_TIME = 3
  global sushi_fail
  print('Started Sushi')
   
  try:
    print('Running Sushi')
    driver=webdriver.Chrome(executable_path=os.getenv('CHROME_EXECUTABLE_PATH'), options=chrome_options)
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
      record.append(i.find( "div" , class_=pool_sushi ).contents[1].contents[0])
      main_dict.append(record) 
      #print(record)
    df = pd.DataFrame(main_dict, columns = ['Pool', 'TVL','APR','Farm Name'])
    df=df[df['Farm Name']!='Kashi Farm']
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

def pangolin():
  print("Started Pangolin")
  url="https://app.pangolin.exchange/#"
  import time
  global pangolin_fail
  chrome_options.add_argument("--start-maximized")
  try:
    
    chrome_options.add_argument('--no-sandbox') 
    chrome_options.add_argument('--disable-dev-shm-usage') 
    driver=webdriver.Chrome(executable_path=os.getenv('CHROME_EXECUTABLE_PATH'), options=chrome_options)

    SCROLL_PAUSE_TIME = 4
    driver.set_window_size(1024, 600)
    driver.maximize_window()
    WebDriverWait(driver, SCROLL_PAUSE_TIME)
    driver.get(url)
    time.sleep(4)
    last_height = 0
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    try:
        print('In')
        element = driver.find_element_by_xpath("//div[@class='sc-bHwgHz cUwfZD']")
        element.click()
        print('click_farm')
        time.sleep(1)
        element = driver.find_element_by_xpath("//span[@class='sc-dNLxif sc-dTdPqK bqUWQk']")    
        element.click()
        time.sleep(6)    
        print('click_a')
    except:
        #print('failed')
        pass

    while True:
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight-500);")

        # Wait to load page
      time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
      new_height = driver.execute_script("return document.body.scrollHeight")
      if new_height == last_height:
          break
      last_height = new_height

      print(new_height,last_height)

    page1 = driver.execute_script('return document.body.innerHTML')
    soup1 = BeautifulSoup(''.join(page1), 'html.parser')
    soup1 = BeautifulSoup(str(soup1).replace('class="sc-gzVnrw bhXWHA"></span>','class="sc-gzVnrw bhXWHA">'))
    soup1 = BeautifulSoup(str(soup1).replace('<span class="sc-gzVnrw bhXWHA"','</span><span class="sc-gzVnrw bhXWHA"'))

    web_data=soup1
    main_list=web_data.find_all("span",class_= "sc-gzVnrw bhXWHA")
    main_dict=[]
    import re
    for i in main_list:
        record=[]
        roww=i
        rowws=str(roww)

        #print(i.contents)
        try:
    
          record.append(roww.contents[0].contents[0].contents[-1].contents[0])

          record.append(roww.contents[1].contents[0].contents[-1].contents[0])

      
          record.append(roww.contents[2].contents[-1].contents[-1].contents[-1])

          record.append(roww.contents[3].contents[-1].contents[-1].contents[-1])

          #record.append(i.find_all( "div" , class_=liqu )[1].contents[0])
          main_dict.append(record) 
        except:
          pass
        #listmirror=[x for x in i.find_all( "span")]
        #i.find_all( "span")
        #print(roww)

        #print(re.search(r'class="AssetItem_symbol__3_Oq5">(.*?)</h1><', str(roww)))
        #print((i.find_all( "span")))
    df = pd.DataFrame(main_dict, columns = ['Pool','Total Staked','Total APR','Pool Weight'])
    #print("Extracted in ",nerve_fail+1,"attempts")
    #print("Extracted ",len(df)," records")
    df.to_csv('Pangolin.csv')


    return df
    print("Extracted in ",pangolin_fail+1,"attempts")
    

  except:
    pangolin_fail=pangolin_fail+1
    print('Failed ',pangolin_fail,' times')
    try:
      initialize()
      
    except:
      pass
    if pangolin_fail<4:
      pangolin()
    else:
      print('Error in Pangolin')
      exit()

      


  return df

def alpaca():
  print("Started alpaca")
  url="https://app.alpacafinance.org/farm"
  #chrome_options = webdriver.ChromeOptions() 
  main_dict=[]

  chrome_options.add_argument('--no-sandbox') 
  chrome_options.add_argument('--disable-dev-shm-usage') 
  chrome_options.add_argument("--start-maximized")
  import time
  global alpaca_fail


  try:
    driver=webdriver.Chrome(executable_path=os.getenv('CHROME_EXECUTABLE_PATH'), options=chrome_options)
    SCROLL_PAUSE_TIME = 2
    driver.maximize_window()
    WebDriverWait(driver, SCROLL_PAUSE_TIME)
    driver.get(url)
    time.sleep(2)
    last_height = 0

    for i in range(1,7):
      time.sleep(SCROLL_PAUSE_TIME)
      try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            #//li[@title='3']
            gts="//li[@title='"+str(i)+"']"
            element = driver.find_element_by_xpath(gts) 
            element.click()
            print(gts,'click')
      except Exception as exx:
        print(exx)
        pass
      page1 = driver.execute_script('return document.body.innerHTML')
      soup1 = BeautifulSoup(''.join(page1), 'html.parser')
      web_data=soup1
      main_list=web_data.find_all("div",class_= "ant-table-container")
      main_list=main_list[0].find_all('tr',class_='ant-table-row ant-table-row-level-0')
      #print(main_list)
      for i in main_list:
        record=[]
        roww=i
        rowws=str(roww)
        record.append(roww.contents[1].contents[0].contents[1].contents[0]) 
        #print(roww)
        record.append(roww.contents[1].contents[-1].contents[-1].contents[1].contents[0])
        record.append(roww.contents[2].contents[0].contents[0].contents[0])   
        record.append(roww.contents[2].contents[0].contents[1].contents[0])
        try:
          record.append(roww.contents[3].contents[-1].contents[3].contents[-1].contents[-1].contents[-1].contents[-1].contents[0].contents[0])
        except:
          record.append(roww.contents[3].contents[-1].find_all('span',class_='c-value')[0].contents[0])
        main_dict.append(record) 
    #print(main_dict)


    df = pd.DataFrame(main_dict, columns = ['Pool Name', 'Liquidity','APY','APY_Cross','Borrowing Interest'])
    df=df.drop_duplicates(subset=['Pool Name'])
    df.to_csv('Alpaca.csv')
  

    return df

    print("Extracted in ",alpaca_fail+1,"attempts")
    

  except:
    alpaca_fail=alpaca_fail+1
    print('Failed ',alpaca_fail,' times')
    try:
      initialize()
      
    except:
      pass
    if alpaca_fail<4:
      alpaca()
    else:
      print('Error in Alpaca')
      exit()

  return df

def All_Crypto():
  #All_websites = pd.DataFrame(columns = ['Pool', 'TVL','APR','source'])
  test_op={'mirror':0,'convex':0,'raydium':0,'balancer':0,'ubeswap':0,'traderjoe':0,'pancake':0,'sushi_nokashi_farm':0,'coingecko':0,'pangolin':0,'alpaca':0}

  try:
    print('Mirror Try 1')
    Mirror_df=mirror()
    print(Mirror_df)
    test_op['mirror']=len(Mirror_df)
  except:
    try:
      initialize()
    except:
      try:
        print('Mirror Try 2')
        Mirror_df=mirror()
        print(Mirror_df)
      except:
        print('Failed to Extract Mirror')    
  
  try:
    print('Convex Try 1')
    Convex_df=convex()
    print(Convex_df)
    test_op['convex']=len(Convex_df)
  except:
    try:
      initialize()
    except:
      try:
        print('Convex Try 2')
        Convex_df=convex()
        print(Convex_df)
        test_op['convex']=len(Convex_df)
      except:
        print('Failed to Extract Convex')    

  try:
    print('raydium Try 1')
    Raydium_df=raydium()
    print(Raydium_df)
    test_op['raydium']=len(Raydium_df)
  except:
    try:
      initialize()
    except:
      try:
        print('raydium Try 2')
        Raydium_df=raydium()
        print(Raydium_df)
        test_op['raydium']=len(Raydium_df)
      except:
        print('Failed to Extract raydium')    

  try:
    print('balancer Try 1')
    Balancer_df=balancer()
    print(Balancer_df)
    test_op['balancer']=len(Balancer_df)
  except:
    try:
      initialize()
    except:
      try:
        print('balancer Try 2')
        Balancer_df=balancer()
        print(Balancer_df)
        test_op['balancer']=len(Balancer_df)
      except:
        print('Failed to Extract balancer')    

  try:
    print('ubeswap Try 1')
    Ubeswap_df=ubeswap()
    print(Ubeswap_df)
    test_op['ubeswap']=len(Ubeswap_df)
  except:
    try:
      initialize()
    except:
      try:
        print('ubeswap Try 2')
        Ubeswap_df=ubeswap()
        print(Ubeswap_df)
        test_op['ubeswap']=len(Ubeswap_df)
      except:
        print('Failed to Extract ubeswap')    

  try:
    print('traderjoe Try 1')
    Traderjoe_df=traderjoe()
    print(Traderjoe_df)
    test_op['traderjoe']=len(Traderjoe_df)
  except:
    try:
      initialize()
    except:
      try:
        print('traderjoe Try 2')
        Traderjoe_df=traderjoe()
        print(Traderjoe_df)
        test_op['traderjoe']=len(Traderjoe_df)        
        
      except:
        print('Failed to Extract traderjoe')    

  try:
    print('pancake Try 1')
    Pancake_df=pancake()
    print(Pancake_df)
    test_op['pancake']=len(Pancake_df)
  except:
    try:
      initialize()
    except:
      try:
        print('pancake Try 2')
        Pancake_df=pancake()
        print(Pancake_df)
        test_op['pancake']=len(Pancake_df)        
      except:
        print('Failed to Extract pancake')    

  try:
    print('sushi_nokashi_farm Try 1')
    Sushi_nokashi_farm_df=sushi_nokashi_farm()
    print(Sushi_nokashi_farm_df)
    test_op['sushi_nokashi_farm']=len(Sushi_nokashi_farm_df)
  except:
    try:
      initialize()
    except:
      try:
        print('sushi_nokashi_farm Try 2')
        Sushi_nokashi_farm_df=sushi_nokashi_farm()
        print(Sushi_nokashi_farm_df)
        test_op['sushi_nokashi_farm']=len(Sushi_nokashi_farm_df)        
      except:
        print('Failed to Extract sushi_nokashi_farm')    

  try:
    print('coingecko Try 1')
    Coingecko_df=coingecko()
    print(Coingecko_df)
    test_op['coingecko']=len(Coingecko_df)
  except:
    try:
      initialize()
    except:
      try:
        print('coingecko Try 2')
        Coingecko_df=coingecko()
        print(Coingecko_df)
        test_op['coingecko']=len(Coingecko_df)        
      except:
        print('Failed to Extract coingecko')    

  try:
    print('pangolin Try 1')
    Pangolin_df=pangolin()
    print(Pangolin_df)
    test_op['pangolin']=len(Pangolin_df)
  except:
    try:
      initialize()
    except:
      try:
        print('pangolin Try 2')
        Pangolin_df=pangolin()
        print(Pangolin_df)
        test_op['pangolin']=len(Pangolin_df)
        
      except:
        print('Failed to Extract pangolin') 
 

  try:
    print('alpaca Try 1')
    Alpaca_df=alpaca()
    print(Alpaca_df)
    test_op['alpaca']=len(Alpaca_df)
  except:
    try:
      initialize()
    except:
      try:
        print('alpaca Try 2')
        Alpaca_df=alpaca()
        print(Alpaca_df)
        test_op['alpaca']=len(Alpaca_df)        
        
      except:
        print('Failed to Extract alpaca') 
 
  return test_op

"""### Execution"""

All_Websites_df=All_Crypto()




missing=[]
for i in All_Websites_df:
    if(All_Websites_df[i]==0):
        missing.append(i)

if(len(missing)>0):
  Failure_Email(missing)



