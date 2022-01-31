import requests
from bs4 import BeautifulSoup as BS
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# url_Peliculas = 'https://www.starz.com/ar/es/movies'
# url_Series = 'https://www.starz.com/ar/es/series'

# pagina = requests.get(url_Peliculas)


#url = 'https://www.starz.com/ar/es/movies' # La url que nos muestra muchos deptos
#search = requests.get(url) # Hacemos el request a la página para acceder a la misma

#print(f'El status es: {search.status_code}') # Chequeamos que haya salido todo bien

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
driver.get("https://www.starz.com/ar/es/movies")
time.sleep(5)

elements = driver.find_elements_by_class_name("view-all")

for iteration in range(6):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(2)


# Ahora guardamos los enlaces de cada elemento
hrefs = []
for element in elements:
    try:
        href = element.find_element_by_tag_name("a").get_attribute("href")
        hrefs.append(href)
    except:
        pass

# # Guardamos los enlaces en un archivo
# fp = open('links.txt','w')
# for href in hrefs:
# 	fp.write(href + '\n')
# fp.close()

# # Finalmente cerramos todas las sesiones de navegación que abrimos. 
# # Son necesarias ambas líneas (una cierra la pestaña, la otra toda el navegador)

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
# print(search_parseada.prettify()[:20000]) # Printeamos los primeros n caracteres para ver qué onda


# tag_deptos = search_parseada.findAll(name = 'div', attrs = {'class' : 'listing__item'})

# soup = BeautifulSoup(pagina.content, 'html.parser') features="html.parser"

# result = soup.find_all(lambda tag: tag.name == 'h6' and tag.get('class') == ['on-hover metadata-items'])


# print(result)


