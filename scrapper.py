from integracion import *
from modelo import *
from conexion import *
from scrapping_homecenter import *
from scrapping_inval import *
from mysql.connector.errors import IntegrityError


def insertar_muebles(lista_muebles):
    
    # Extraemos los muebles que estan en la base de datos
    query_select_muebles = "SELECT referencia FROM mueble"
    lista_muebles_db = ejecutar_consulta(query_select_muebles)
    
    lista_referencias_db = list()
    
    for referencia in lista_muebles_db:
        lista_referencias_db.append(referencia[0])
    
    lista_referencias_scrapping = list()
    
    for mueble in lista_muebles:
        lista_referencias_scrapping.append(mueble.referencia)
    
    # Items nuevos y las actualizaciones
    for mueble in lista_muebles:
        if mueble.precio == "":
            mueble.precio = 0
        if mueble.peso == "":
            mueble.peso = 0
        if mueble.ancho == "":
            mueble.ancho = 0
        if mueble.alto == "":
            mueble.alto = 0
        if mueble.fondo == "":
            mueble.fondo = 0
        
        if mueble.referencia not in lista_referencias_db:
            query_insercion = ("INSERT INTO mueble "
                "(referencia, categoria, precio, peso, ancho, alto, profundo, urls, observaciones, estado) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
            
            datos_insercion = (
                    mueble.referencia,
                    mueble.categoria, 
                    mueble.precio,
                    mueble.peso,
                    mueble.ancho,
                    mueble.alto,
                    mueble.fondo,
                    " ".join(mueble.urls),
                    mueble.observaciones,
                    mueble.estado 
            )
            try:
                ejecutar_insercion(query_insercion, datos_insercion)
            except IntegrityError:
                print("Entrada duplicada")
            
        else:
           query_actualizacion = ("UPDATE mueble "
                "SET categoria=%s, precio=%s, peso=%s, ancho=%s, alto=%s, profundo=%s, urls=%s, observaciones=%s, estado=%s "
                "WHERE referencia=%s") 
           
           datos_actualizacion = (
                    mueble.categoria, 
                    mueble.precio,
                    mueble.peso,
                    mueble.ancho,
                    mueble.alto,
                    mueble.fondo,
                    " ".join(mueble.urls),
                    mueble.observaciones,
                    mueble.estado, 
                    mueble.referencia,
            )
           
           ejecutar_actualizacion(query_actualizacion, datos_actualizacion)
           
    # Items inactivos
    for referencia in lista_referencias_db:
        if referencia not in lista_referencias_scrapping:
            query_inactivacion = "UPDATE mueble SET estado=0 WHERE referencia=%s"
            datos_inactivacion = (referencia, )
            ejecutar_actualizacion(query_inactivacion, datos_inactivacion)
    

    


def poblar_db():
    #print("==> Cargando base de datos Inval")
    lista_inval = [] #extraer_muebles_inval()
    
    print("==> Cargando base de datos Homecenter")
    lista_homecenter = extraer_muebles_homecenter()

    print("==> Integrando bases de datos")
    lista_integrada = integrar_scrappers(lista_inval, lista_homecenter)
    
    print("==> Actualizando base de datos")
    insertar_muebles(lista_integrada)
    print("==> Base de datos actualizada")