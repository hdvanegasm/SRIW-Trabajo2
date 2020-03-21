import requests
import html5lib

from bs4 import BeautifulSoup
from modelo import *

def valorcitotofloat(valorcito):
  if "milímetros" in valorcito:
    if "Hasta" in valorcito:
      valorcito = float(str(''.join(filter(lambda i: i.isdigit() or i == "." or i == ",", valorcito.text.strip())))) * 0.1
    else:
      valorcito = float(valorcito.text.strip().split()[0].replace(",", ".")) * 0.1
  else:
    if "Hasta" in valorcito:
      valorcito = float(str(''.join(filter(lambda i: i.isdigit() or i == "." or i == ",", valorcito.text.strip()))))
    else:
      valorcito = float(valorcito.text.strip().split()[0].replace(",", "."))
  return(valorcito) 
  
def extraer_muebles_homecenter():
  lista_muebles = []

  for pagina in range (1,4):
    URL = 'https://www.homecenter.com.co/homecenter-co/search/?Ntt=inval&sTerm=inval&sType=suggest&sScenario=BTP_SUG_inval&currentpage=' + str(pagina)
    page = requests.get(URL)
    parser = BeautifulSoup(page.content, 'html.parser')
    lista = parser.find('div', class_='jsx-3663142191 search-results-products-container')
  
    for i in lista:
      referencia = ""
      ancho = ""
      alto = ""
      fondo = ""
      precio = ""
      peso = ""
      tipo = ""

      info = i.find('div', class_='jsx-1061017191 product ie11-product-container')
      price = i.find('div', class_='jsx-3236283393 price jsx-175035124')
      titulo = info.find('h2', class_='jsx-1061017191 product-title')
      link = info.find('a', class_='jsx-1061017191')
      link = link['href']
      link = ("https://www.homecenter.com.co" + link)

      precio = price.text.strip()
      precio = int(str(''.join(filter(lambda i: i.isdigit(), precio))))

      URL2 = link
      #URL2 = "https://www.homecenter.com.co/homecenter-co/product/415024/Comoda-3-Cajones-75x80x37-5cm-Amaretto/415024"
      page = requests.get(URL2)
      parser = BeautifulSoup(page.content, 'html.parser')
      ancho = ''
      alto = ''
      fondo = ''
      tipo = ''
      peso = ''
      referencia = ''
  

      lista2 = parser.find('div', class_='simple-table')
      caracteristica = lista2.find_all('div', class_='row')
      for caracteristica in lista2:
        titulito = caracteristica.find('div', class_='title').text
        valorcito = caracteristica.find('div', class_='value')
        
        #print(titulito, ' ', valorcito)
        if 'Tipo' in titulito:
          tipo = valorcito.text
        if 'Alto' in titulito:
          if 'Rango' not in titulito:
            alto = valorcitotofloat(valorcito)
        if 'Ancho' in titulito:
          if 'Rango' not in titulito:
            ancho = valorcitotofloat(valorcito)
        if 'Fondo' in titulito or 'Largo' in titulito:
          if 'Rango' not in titulito:
            fondo = valorcitotofloat(valorcito)
        if 'Peso del producto' in titulito:
          if 'Rango' not in titulito:
            peso = valorcitotofloat(valorcito)
        if 'Referencia' in titulito:
          referencia = valorcito.text.split('-')[0]
      #print(tipo, '', alto, '',ancho, '',fondo, '',peso, '',referencia)      
      if referencia != "":  
        mueble = Mueble(referencia, tipo, precio, peso, ancho, alto, fondo, [link])
        lista_muebles.append(mueble)

  return lista_muebles
