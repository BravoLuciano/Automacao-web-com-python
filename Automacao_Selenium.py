from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

try:
    barra_busca = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input')
    barra_busca.send_keys("standard_user")

    barra_busca = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input')
    barra_busca.send_keys("secret_sauce")

    botao_busca = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/input')
    botao_busca.click()

    botao_busca = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button')
    botao_busca.click()

    botao_busca = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/button')
    botao_busca.click()

    botao_busca = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[6]/div[2]/div[2]/button')
    botao_busca.click()

    botao_busca = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div[3]/a')
    botao_busca.click()

    botao_busca = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/button[2]')
    botao_busca.click()
    sleep(5)
    barra_busca = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[1]/div[1]/input')
    barra_busca.send_keys("Pedro")
    sleep(1)
    barra_busca = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[1]/div[2]/input')
    barra_busca.send_keys("Silas")
    sleep(1)
    barra_busca = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[1]/div[3]/input')
    barra_busca.send_keys("13465-000")
    sleep(1)
    botao_busca = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[2]/input')
    botao_busca.click()
    sleep(1)

    botao_busca = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div[9]/button[2]')
    botao_busca.click()
    sleep(5)
except NoSuchElementException:
    print('Elemento não Encontrado')
except Exception as e:
    print('Tente mais tarde novamente')

