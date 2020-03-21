from modelo import *

def encontrar_mueble(mueble, lista):
  for elemento in lista:
    if mueble == elemento:
      return elemento
  

def integrar_scrappers(muebles_inval, muebles_homecenter):
 
  # Completa los atributos de los elementos de inval
  for mueble in muebles_inval:
    if mueble.categoria == "" and mueble in muebles_homecenter:
      mueble_home = encontrar_mueble(mueble, muebles_homecenter)
      if mueble_home.categoria != "":
        mueble.categoria = mueble_home.categoria
        mueble.observaciones += "Único valor de característica para %s, valor faltante en %s\n\n" % ("Categoria", "www.inval.com.co")
      
    if mueble.precio == "" and mueble in muebles_homecenter:
      mueble_home = encontrar_mueble(mueble, muebles_homecenter)
      if mueble_home.precio != "":
        mueble.precio = mueble_home.precio
        mueble.observaciones += "Único valor de característica para %s, valor faltante en %s\n\n" % ("Precio", "www.inval.com.co")
        
    if mueble.peso == "" and mueble in muebles_homecenter:
      mueble_home = encontrar_mueble(mueble, muebles_homecenter)
      if mueble_home.peso != "":
        mueble.peso = mueble_home.peso
        mueble.observaciones += "Único valor de característica para %s, valor faltante en %s\n\n" % ("Peso", "www.inval.com.co")
       
    if mueble.ancho == "" and mueble in muebles_homecenter:
      mueble_home = encontrar_mueble(mueble, muebles_homecenter)
      if mueble_home.ancho != "":
        mueble.ancho = mueble_home.ancho
        mueble.observaciones += "Único valor de característica para %s, valor faltante en %s\n\n" % ("Ancho", "www.inval.com.co")
        
    if mueble.alto == "" and mueble in muebles_homecenter:
      mueble_home = encontrar_mueble(mueble, muebles_homecenter)
      if mueble_home.alto != "":
        mueble.alto = mueble_home.alto
        mueble.observaciones += "Único valor de característica para %s, valor faltante en %s\n\n" % ("Alto", "www.inval.com.co")
        
    if mueble.fondo == "" and mueble in muebles_homecenter:
      mueble_home = encontrar_mueble(mueble, muebles_homecenter)
      if mueble_home.fondo != "":
        mueble.fondo = mueble_home.fondo
        mueble.observaciones += "Único valor de característica para %s, valor faltante en %s\n\n" % ("Fondo", "www.inval.com.co")
        
  # Completa los atributos de los elementos de homecenter
  for mueble in muebles_homecenter:
    if mueble.categoria == "" and mueble in muebles_inval:
      mueble_inval = encontrar_mueble(mueble, muebles_inval)
      if mueble_inval.categoria != "":
        mueble.categoria = mueble_inval.categoria
        mueble.observaciones += "Único valor de característica para %s, valor faltante en %s\n\n" % ("Categoría", "www.homecenter.com.co")
       
    if mueble.precio == "" and mueble in muebles_inval:
      mueble_inval = encontrar_mueble(mueble, muebles_inval)
      if mueble_inval.precio != "":
        mueble.precio = mueble_inval.precio
        mueble.observaciones += "Único valor de característica para %s, valor faltante en %s\n\n" % ("Precio", "www.homecenter.com.co")
        
    if mueble.peso == "" and mueble in muebles_inval:
      mueble_inval = encontrar_mueble(mueble, muebles_inval)
      if mueble_inval.peso != "":
        mueble.peso = mueble_inval.peso
        mueble.observaciones += "Único valor de característica para %s, valor faltante en %s\n\n" % ("Peso", "www.homecenter.com.co")
       
    if mueble.ancho == "" and mueble in muebles_inval:
      mueble_inval = encontrar_mueble(mueble, muebles_inval)
      if mueble_inval.ancho != "":
        mueble.ancho = mueble_inval.ancho
        mueble.observaciones += "Único valor de característica para %s, valor faltante en %s\n\n" % ("Ancho", "www.homecenter.com.co")
       
    if mueble.alto == "" and mueble in muebles_inval:
      mueble_inval = encontrar_mueble(mueble, muebles_inval)
      if mueble_inval.alto != "":
        mueble.alto = mueble_inval.alto
        mueble.observaciones += "Único valor de característica para %s, valor faltante en %s\n\n" % ("Alto", "www.homecenter.com.co")

    if mueble.fondo == "" and mueble in muebles_inval:
      mueble_inval = encontrar_mueble(mueble, muebles_inval)
      if mueble_inval.fondo != "":
        mueble.fondo = mueble_inval.fondo
        mueble.observaciones += "Único valor de característica para %s, valor faltante en %s\n\n" % ("Fondo", "www.homecenter.com.co")



  lista_integrada = []

  # Agrega los muebles de homecenter que no estan en Inval

  for mueble in muebles_homecenter:
    if mueble not in muebles_inval:
      lista_integrada.append(mueble)
    else:
      mueble_inval = encontrar_mueble(mueble, muebles_inval)
      mueble.urls.append(mueble_inval.urls[0])

      # Verificación de diferencias
      if mueble_inval.categoria != mueble.categoria:
        mueble.observaciones += "Diferencia de valor encontrado para %s. Se selecciona el valor %s. Posibles valores: %s en %s y %s en %s \n\n"  % ("Categoría", mueble.categoria, mueble.categoria, "www.homecenter.com", mueble_inval.categoria, "www.inval.com.co")
      
      if mueble_inval.precio != mueble.precio:
        mueble.observaciones += "Diferencia de valor encontrado para %s. Se selecciona el valor %s. Posibles valores: %s en %s y %s en %s \n\n" % ("Precio", mueble.precio, mueble.precio, "www.homecenter.com", mueble_inval.precio, "www.inval.com.co")

      if mueble_inval.peso != mueble.peso:
        mueble.observaciones += "Diferencia de valor encontrado para %s. Se selecciona el valor %s. Posibles valores: %s en %s y %s en %s \n\n" % ("Peso", mueble.peso, mueble.peso, "www.homecenter.com", mueble_inval.peso, "www.inval.com.co")

      if mueble_inval.ancho != mueble.ancho:
        mueble.observaciones += "Diferencia de valor encontrado para %s. Se selecciona el valor %s. Posibles valores: %s en %s y %s en %s \n\n" % ("Ancho", mueble.ancho, mueble.ancho, "www.homecenter.com", mueble_inval.ancho, "www.inval.com.co")

      if mueble_inval.alto != mueble.alto:
        mueble.observaciones += "Diferencia de valor encontrado para %s. Se selecciona el valor %s. Posibles valores: %s en %s y %s en %s \n\n" % ("Alto", mueble.alto, mueble.alto, "www.homecenter.com", mueble_inval.alto, "www.inval.com.co")

      if mueble_inval.fondo != mueble.fondo:
        mueble.observaciones += "Diferencia de valor encontrado para %s. Se selecciona el valor %s. Posibles valores: %s en %s y %s en %s \n\n" % ("Fondo", mueble.fondo, mueble.fondo, "www.homecenter.com", mueble_inval.fondo, "www.inval.com.co")

      lista_integrada.append(mueble)

  for mueble in muebles_inval:
    if mueble not in lista_integrada:
      lista_integrada.append(mueble)
  

  return lista_integrada