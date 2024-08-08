from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

driver = webdriver.Chrome()
driver.get('https://books.toscrape.com/')


livros = driver.find_elements(By.XPATH, '//article[@class="product_pod"]')

for livro in livros:
    link = livro.find_element(By.XPATH, './h3/a')
    link.click()
    sleep(1)
    
    titulo = driver.find_element(By.TAG_NAME, 'h1')
    preco = driver.find_element(By.XPATH, './/p[@class="price_color"]')
    estoque = driver.find_element(By.XPATH, './/p[@class="instock availability"]')

    print(titulo.text)
    print(preco.text)
    print(estoque.text)

    driver.back()
    sleep(5)
                               

