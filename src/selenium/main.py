from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import login

driver = webdriver.Chrome()

driver.get("https://sigaa.sistemas.ufcat.edu.br/sigaa/verTelaLogin.do")

print(driver.title)

login_user = driver.find_element(By.NAME, "user.login")
login_user.send_keys(login.user)

login_password = driver.find_element(By.NAME, "user.senha")
login_password.send_keys(login.senha)
login_password.send_keys(Keys.RETURN)
time.sleep(5)

driver.quit()
