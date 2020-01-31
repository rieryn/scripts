#attempts to login to poshmark through google account using selenium
#currently only works on new accounts due to automation detection, trying to find a workaround
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_path = r"C:\Users\Guest1\PycharmProjects\selenium scraper\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("http://www.poshmark.ca/login")

#for user to change
username = input_email
password = input_password

windows_before = driver.current_window_handle;
print (windows_before)

google_login_button = driver.find_element_by_id("gp-auth-btn")
google_login_button.click()
WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

windows_after = driver.window_handles
new_window = [x for x in windows_after if x != windows_before][0]
driver.switch_to.window(new_window)
print("Page Title after Tab Switching is : %s" %driver.title)
print("Second Window Handle is : %s" %new_window)
driver.implicitly_wait(10)
element = driver.find_element_by_xpath("//*[@id='Email']").send_keys(username)
driver.find_element_by_id("next").click()
#driver.switch_to_window(window_before)
driver.find_element_by_id("Passwd").send_keys(password)
 
