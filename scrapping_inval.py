from modelo import *

import requests 
from bs4 import BeautifulSoup 

def datosMueble(cadena, stringCategoria):
    URL = cadena
    page = requests.get(URL) 
    parser = BeautifulSoup(page.content, 'html.parser') 

    
    referencia = parser.find('h2', class_='referencia tx-sz-lg').text.strip()
    
    categoria = parser.find('nav', class_='breadcrumb')
    categoria = categoria.find_all('li')
    if len(categoria)==4:
        categoria = categoria[2]
        categoria = categoria.find('span', itemprop='name').text.strip()
    else:
        categoria = stringCategoria 

    
    datos = parser.find('dl',class_='data-sheet').find_all('dd',class_='value') 
    datosn = parser.find('dl',class_='data-sheet').find_all('dt',class_='name') 

    i=0
    alto=''
    ancho=''
    profundidad=''
    peso=''
    for dato in datosn:
        if dato.text.strip()=='Altura':
            alto = float(datos[i].text.strip()
              .replace(" cm", "")
              .replace("cm", "")
              .replace(" CM", "")
              .replace(",", "."))
        elif dato.text.strip()=='Ancho':
            ancho = float(datos[i].text.strip()
              .replace(" cm", "")
              .replace("cm", "")
              .replace(" CM", "")
              .replace(",", "."))
        elif dato.text.strip()=='Profundidad':
            profundidad = float(datos[i].text.strip()
              .replace(" cm", "")
              .replace("cm", "")
              .replace(" CM", "")
              .replace(",", "."))
        elif dato.text.strip()=='Peso':
            peso = float(datos[i].text.strip().replace(" kg", "")
              .replace(",", ".")
              .replace("Kg", ""))
        i+=1
    precio = parser.find('span', class_='price')
    precio = int(precio['content']) 

    referencia = referencia \
      .split("-")[0].strip()

    return Mueble(referencia, categoria, precio, peso, ancho, alto, profundidad, [cadena])


def buscarMuebles(cadena, categoria):
    URL = cadena+'?page=1'
    link = ''
    lista_muebles = list()
    while URL != link:
        link=URL
        page = requests.get(URL) 
        parser = BeautifulSoup(page.content, 'html.parser') 
        muebles = parser.find('div', class_='products row product_content grid')
        muebles = muebles.find_all('div', class_='item-product')
        for mueble in muebles:
            mueble = mueble.find('a')['href']
            mueble_obj = datosMueble(mueble,categoria)
            lista_muebles.append(mueble_obj)

        URL = parser.find('a', rel='next')['href']

    return lista_muebles


def extraer_muebles_inval():
    URL = 'https://inval.com.co/col/'
    page = requests.get(URL) 
    parser = BeautifulSoup(page.content, 'html.parser') 
    muebles = parser.find_all('div', class_='pt_menu')
    lista_definitiva = []
    for mueble in muebles:
        a = mueble.find_all('a', class_='itemMenuName')
        for cat in a:
            link = cat['href']
            categoria = cat.text
            lista_muebles_cat = buscarMuebles(link, categoria)
            lista_definitiva += lista_muebles_cat
    
    return lista_definitiva

