from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

driver = webdriver.Chrome()
driver.get('https://books.toscrape.com/')

titulo = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/section/div[2]/ol/li[1]/article/h3/a')
titulo.click()
sleep(1)

titulo_especifico = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/article/div[1]/div[2]/h1')
print(titulo_especifico.text)

driver.back()
sleep(5)

titulo2 = driver.find_element(By.XPATH, '/html/body/div/div/div/div/section/div[2]/ol/li[14]/article/h3/a')
titulo2.click()
sleep(1)

titulo3 = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/article/div[1]/div[2]/h1')
print(titulo3.text)
driver.back()
sleep(5)
