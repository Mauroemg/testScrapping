from xml.dom.minidom import Element
from attr import attrs
import requests
from bs4 import BeautifulSoup as BS
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


##################################
path_driver = 'C:/Users/Admin/scrappers/chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument("--headless")


# Creación del navegador
driver = webdriver.Chrome(executable_path = path_driver, options = chrome_options)

# Visitamos la página y esperamos 5 segundos a que todo cargue bien
driver.get("https://www.starz.com/ar/es/movies")
time.sleep(5)

#scroleamos la pagina un par de veces
for iteration in range(6):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(2)

soup = BS(driver.page_source, features="html.parser")
#print(soup)

# for caption in soup.find_all(class_='caption'):
#     product_name = caption.find(class_='title').text
#     price = caption.find(class_='pull-right price').text
#     print(product_name, price)

soup.prettify


#elements = soup.find_all(attrs = {"class": "view-all"}, href)
elemeee = soup.find( href=True, class_="view-all")["href"]
print(elemeee)



# articles = [e.a.attrs['href'] for e in elements]
# print(articles)



# Ahora guardamos los enlaces de cada elemento

# count = 1
# hrefs = []
# for element in elements:
#     try:
#         href = element.
#         hrefs.append(href)
#     except:
#         pass


# print(hrefs)



# # Guardamos los enlaces en un archivo
# fp = open('links.txt','w')
# for href in hrefs:
# 	fp.write(href + '\n')
# fp.close()



driver.close()
driver.quit()






# urls = []
# for element in elements:
#     try:
#         urls.append(element.find('h6')['class'])
#     except:
#         pass

# print(urls)

# print(len(urls))

# search_parseada = bs(search.content, 'html.parser') # Parseamos el contenido del request como un html
# print(search_parseada.prettify()[:20000]) #


# tag_deptos = search_parseada.findAll(name = 'div', attrs = {'class' : 'listing__item'})

# soup = BeautifulSoup(pagina.content, 'html.parser') features="html.parser"

# result = soup.find_all(lambda tag: tag.name == 'h6' and tag.get('class') == ['on-hover metadata-items'])


# print(result)


# from selenium import webdriver
# from bs4 import BeautifulSoup
# import time

# driver = webdriver.Chrome()
# driver.get('http://www.simon.com/mall')
# time.sleep(3)

# soup = BeautifulSoup(driver.page_source, 'lxml')
# driver.quit()

# for item in soup.find_all(class_="mall-list-item-text"):
#     name = item.find_all(class_='mall-list-item-name')[0].text
#     location = item.find_all(class_='mall-list-item-location')[0].text
#     print(name,location)