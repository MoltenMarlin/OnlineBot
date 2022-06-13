'''
Alex
Bot Program for Amazon
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import random


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False) 
#options.add_argument('--headless')
options.add_argument("user-data-dir=C:/Users/Alex/AppData/Local/Google/Chrome/User Data")
options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome('C:/chromedriver.exe', options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get("https://www.amazon.com/dp/B08HHDP9DW/?coliid=I3FSKH16WR7GUO&colid=3PM8NMET43SN6&psc=0&ref_=lv_ov_lig_dp_it")
rando = (random.uniform(2.7, 5.2))
refreshee = (random.uniform(25.6, 35.7))
randScroll = random.randint(240,600)
time.sleep(rando)

a = driver.find_element_by_xpath
b = driver.find_elements_by_xpath


while len(b('//*[@id="add-to-cart-button"]')) == 0:
    print('Not found')
    time.sleep(refreshee)
    driver.refresh()
    driver.execute_script("window.scrollTo(0,"+str(randScroll)+");") 

a('//*[@id="add-to-cart-button"]').click()

#This is option for warranty... if it exists click no
time.sleep(rando)
if len(b('//*[@id="siNoCoverage-announce"]')) > 0:
    a('//*[@id="siNoCoverage-announce"]').click()

time.sleep(rando)

#go to the cart 
a('//*[@id="nav-cart-count-container"]').click()
time.sleep(rando)
a('//*[@id="sc-buy-box-ptc-button"]/span/input').click()
time.sleep(rando)

#if prime sign up is asked then click no
if len(b('//*[@id="signup_cancel"]')) > 0:
    a('//*[@id="signup_cancel"]').click()
    
time.sleep(rando)

#apply discover cashback to purchase
a('//*[@id="inline-points-button"]/span/span[1]').click()
time.sleep(rando)

#free shipping option
a('//*[@id="spc-orders"]/div[1]/div/div[3]/div/div/div[2]/div[2]/div[1]/fieldset/div[2]/input').click()
time.sleep(rando)


'''
#place order
a('//*[@id="placeYourOrder"]/span/input')
'''

#Sign in to amazon
url = ("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcss%2Fhomepage.html%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
driver.get(url)

time.sleep(1.1)
driver.find_element_by_xpath('//*[@id="ap_email"]').send_keys('email@gmail.com')
time.sleep(1.9)
driver.find_element_by_xpath('//*[@id="continue"]').click()

driver.find_element_by_xpath('//*[@id="ap_password"]').send_keys('password')
time.sleep(1.6)
driver.find_element_by_xpath('//*[@id="signInSubmit"]').click()
time.sleep(.75)
driver.find_element_by_xpath('//*[@id="authportal-main-section"]/div[2]/div/div/div/form/div/div[2]/div/div/label/div/label/input').click()

driver.get("https://sslproxies.org/")
driver.find_element_by_xpath('//*[@id="proxylisttable_filter"]/label/input').send_keys('United States elite')
time.sleep(2)

#ips = driver.find_element_by_xpath('//*[@id="proxylisttable"]/tbody/tr[1]/td[1]').text
#ports = driver.find_element_by_xpath('//*[@id="proxylisttable"]/tbody/tr[1]/td[2]').text
ips = [my_elem.get_attribute("innerHTML") for my_elem in WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-striped table-bordered dataTable']//tbody//tr[@role='row']/td[position() = 1]")))]
ports = [my_elem.get_attribute("innerHTML") for my_elem in WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-striped table-bordered dataTable']//tbody//tr[@role='row']/td[position() = 2]")))]
driver.quit()


#PROXY SETUP NOT FINISHED
'''
proxies = []
for i in range(0, len(ips)):
    proxies.append(ips[i]+':'+ports[i])
print(proxies)

for i in range(0, len(proxies)):
    try:
        options.add_argument('--proxy-server={}'.format(proxies[i]))
        driver = webdriver.Chrome(options=options, executable_path=r'C:/Users/molte/Downloads/chromedriver_win32/chromedriver.exe')
        driver.get("https://amazon.com/")
        print('YAH')
    except Exception:
        driver.quit()

'''
