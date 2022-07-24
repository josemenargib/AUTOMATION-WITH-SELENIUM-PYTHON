from lib2to3.pgen2.driver import Driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
import time, json

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
driver.get("https://thetestingworld.com/shop/index.php?route=account/register")

#with open("employees.json") as json_file:
    #data = json.load(json_file)

    #for p in data["employees"]:

        #print(p["name"] + " is loading!")

time.sleep(3)

PrimerNombre = driver.find_element(By.XPATH, "//*[@id='input-firstname']")
PrimerNombre.send_keys("jose")

Apellido = driver.find_element(By.XPATH, "//*[@id='input-lastname']")
Apellido.send_keys("menar")
Email = driver.find_element(By.XPATH, "//*[@id='input-email']")
Email.send_keys("josse001101001101@gmail.com")

Telefono = driver.find_element(By.XPATH, "//*[@id='input-telephone']")
Telefono.send_keys("5878885")

Password = driver.find_element(By.XPATH, "//*[@id='input-password']")
Password.send_keys("picachu")
ContConf = driver.find_element(By.XPATH, "//*[@id='input-confirm']")
ContConf.send_keys("picachu")

driver.find_element(By.XPATH, "//*[@name='agree']").click()

driver.find_element(By.XPATH, "//*[@class='btn btn-primary']").click()
#Pol_Priv.send_keys(Keys.ENTER)

#Continuar = driver.find(By.XPATH, "//*[@Class='btn btn-primary']")
#Continuar.click()

        #print(p["name"] + " is done!")

time.sleep(5)


driver.quit()