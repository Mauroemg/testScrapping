import requests
from bs4 import BeautifulSoup as BS
import pandas as pd
from selenium import * 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

# url_Peliculas = 'https://www.starz.com/ar/es/movies'
# url_Series = 'https://www.starz.com/ar/es/series'

# pagina = requests.get(url_Peliculas)


#url = 'https://www.starz.com/ar/es/movies' #
#search = requests.get(url) #
#print(f'El status es: {search.status_code}')

#print(search.content)


#soup = BS(search.content, features="html.parser")

#soup.prettify


#elements = soup.find_all(attrs = {"class": "on-hover metadata-items"})
#print(elements)


##################################
path_driver = 'C:/Users/Admin/scrappers/chromedriver.exe'
chrome_options = Options()
#chrome_options.add_argument("--headless")


# Creación del navegador
driver = webdriver.Chrome(executable_path = path_driver, options = chrome_options)


# Visitamos la página y esperamos 5 segundos a que todo cargue bien
driver.get("https://www.lanacion.com.ar/")
time.sleep(5)

elements = driver.find_elements_by_class_name("com-title --xs")


for iteration in range(6):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(2)

# Ahora guardamos los enlaces de cada elemento
hrefs = []
for element in elements:
    try:
        href = element.find_elements_by_tag_name('a')
    
        hrefs.append(href)
    except:
        pass


print(hrefs)

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
# print(search_parseada.prettify()[:20000]) 


# tag_deptos = search_parseada.findAll(name = 'div', attrs = {'class' : 'listing__item'})

# soup = BeautifulSoup(pagina.content, 'html.parser') features="html.parser"

# result = soup.find_all(lambda tag: tag.name == 'h6' and tag.get('class') == ['on-hover metadata-items'])


# print(result)


