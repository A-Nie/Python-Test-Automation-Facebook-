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
print("Opened Facebook...")
email = driver.find_element_by_id('email')
email.click()
email.send_keys(username)
print("Email or phone number entered...")
# driver.maximize_window()  # maximizes browser window

passw = driver.find_element_by_id('pass')
passw.click()
passw.send_keys(password)
passw.send_keys(Keys.RETURN)
print("Password Accepted")
print("Signed...")

profile = driver.find_element_by_xpath("//span[@class='_1vp5'][contains(.,'Adi')]")  # entry into the profile via XPath
profile.click()
time.sleep(3)  # delay of transition to the next step in seconds
main_page = driver.find_element_by_xpath(
    "//a[@href='https://www.facebook.com/?ref=tn_tnmn']")  # back to main page facebook
main_page.click()
time.sleep(3)
news = driver.find_element_by_xpath("//div[@dir='ltr'][contains(.,'Aktualności')]")  # entering to news
news.click()
time.sleep(2)

status = driver.find_element_by_xpath("//textarea[@name='xhpc_message']")  # adding a new post
status.send_keys("Tested by Adi!!")  # entering anything
print("Status testing...")
time.sleep(3)

print("Test passed!")
driver.quit()  # closes the browser window
