
import mysql.connector
import pandas as pd

conexion_db = mysql.connector.connect(
   user="root", 
   password="", 
   host="127.0.0.1",
   database="muebles"
)

def insertar_muebles(lista_muebles):
    for mueble in lista_muebles:
        query_insercion = ("INSERT INTO mueble
            "(referencia, categoria, precio, peso, ancho, alto")