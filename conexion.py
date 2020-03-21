
import mysql.connector
import pandas as pd

conexion_db = mysql.connector.connect(
   user="root", 
   password="", 
   host="127.0.0.1",
   database="muebles"
)

def ejecutar_consulta(query):
    cursor = conexion_db.cursor()
    cursor.execute(query)
    
    resultados = list()
    
    for resultado in cursor:
        resultados.append(resultado)
        
    cursor.close()
    return resultados
    
def ejecutar_actualizacion(query, datos):
    """
    La variable datos es una tupla con los datos a actualizar y los que estan en el where
    """
    cursor = conexion_db.cursor()
    cursor.execute(query, datos)
    conexion_db.commit()
    cursor.close()

def ejecutar_insercion(query, datos):
    """
    La variable datos es una tupla con los datos a insertar
    """
    cursor = conexion_db.cursor()
    cursor.execute(query, datos)
    conexion_db.commit()
    cursor.close()
    
    


