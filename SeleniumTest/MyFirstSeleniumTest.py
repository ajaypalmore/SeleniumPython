import time
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="D:\\driver\\Chromedriver.exe")
#driver = webdriver.Firefox(executable_path="D:\\driver\\geckodriver.exe")
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("http://www.newtours.demoaut.com/")
print("Page Title >>> "+driver.title)
ele_username = driver.find_element_by_name("userName")
ele_pwd = driver.find_element_by_name("password")
btn_signIn = driver.find_element_by_name("login")

ele_username.send_keys("mercury")
ele_pwd.send_keys("mercury")
btn_signIn.click()
print("Page Title >>> "+driver.title)


time.sleep(5)
driver.close()
