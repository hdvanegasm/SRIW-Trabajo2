class Mueble:

  def __init__(self, referencia, categoria, precio, peso, ancho, alto, fondo, urls=[], observaciones="", estado=1):
    self.referencia = referencia
    self.categoria = categoria
    self.precio = precio
    self.peso = peso
    self.ancho = ancho
    self.alto = alto
    self.fondo = fondo
    self.observaciones = observaciones
    self.estado = estado
    self.urls = urls

  def __eq__(self, otro):
    return self.referencia == otro.referencia
  

class Usuario:
  
  def __init__(self, correo, nombre, contrasena):
    self.correo = correo
    self.contrasena = contrasena
    self.nombre = nombre


class Calificacion:
  
  def __init__(self, correo_usuario, mueble_referencia, puntaje):
    self.correo_usuario = correo_usuario
    self.mueble_referencia = mueble_referencia
    self.puntaje = puntaje