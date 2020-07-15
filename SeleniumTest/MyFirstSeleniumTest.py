import time
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path="D:\\driver\\Chromedriver.exe")
#driver = webdriver.Firefox(executable_path="D:\\driver\\geckodriver.exe")
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("https://freecrm.co.in/")
print("Page Title >>> "+driver.title)
assert "Free CRM #1 cloud software for any business large or small" in driver.title
link_login = driver.find_element_by_xpath("//a[@class='btn btn-primary btn-xs-2 btn-shadow btn-rect btn-icon btn-icon-left']")
link_login.click()
print("Page Title >>> "+driver.title)
ele_username = driver.find_element_by_name("email")
ele_pwd = driver.find_element_by_name("password")
btn_signIn = driver.find_element_by_xpath("//div[@class='ui fluid large blue submit button']")

print ("UserName :::",ele_username.is_enabled())
print ("Password :::",ele_pwd.is_enabled())
print ("Sign In :::",btn_signIn.is_enabled())

print ("UserName :::",ele_username.is_displayed())
print ("Password :::",ele_pwd.is_displayed())
print ("Sign In :::",btn_signIn.is_displayed())

ele_username.send_keys("ajaypalmore@gmail.com")
ele_pwd.send_keys("Ajay1234")

wait = WebDriverWait(driver,10)
ele = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='ui fluid large blue submit button']")))
ele.click()

print("Page Title >>> "+driver.title)

assert "Ajay More" in driver.find_element_by_xpath("//div/span[text()='Ajay More']").text

time.sleep(5)
driver.close()
