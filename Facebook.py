import time  # impotring time for function "time.sleep()"
from selenium import webdriver  # importing selenium webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass  # hiding the password

username = input("Nazwa użytkownika:")
password = getpass("Hasło:")

DRIVER_PATH = r'C:\Users\NodyBajNydże\Desktop\py\chromedriver.exe'  # enter your path to the chromedriver

options = webdriver.ChromeOptions()  # initiating options for Chrome
options.add_argument('disable-notifications')  # exclusion of notification
options.add_argument('disable-infobars')  # turning off the infobar

driver = webdriver.Chrome(DRIVER_PATH, options=options)
driver.get('https://facebook.com')
email = driver.find_element_by_id('email')
email.click()
email.send_keys(username)
driver.maximize_window() #maximizes browser window

passw = driver.find_element_by_id('pass')
passw.click()
passw.send_keys(password)
passw.send_keys(Keys.RETURN)

time.sleep(2)  # delay of transition to the next step in seconds
profile = driver.find_element_by_xpath("//span[@class=''][contains(.,'')]")  #entry into the profile via XPath
profile.click()

driver.quit()  # closes the browser window
