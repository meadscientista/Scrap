from selenium import webdriver
print('1')
EXTENSION_PATH = 'mask.crx'
print('2')
opt = webdriver.ChromeOptions()
print('3')
opt.add_extension(EXTENSION_PATH)
print('4')
driver = webdriver.Chrome(chrome_options=opt)
print('5')
time.sleep(10)
print('6')
#driver.maximize_window()

driver.switch_to.window(driver.window_handles[0])
driver.switch_to.window(driver.window_handles[0])
driver.switch_to.window(driver.window_handles[1])
print('Window Switched')
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
