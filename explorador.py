from conexion import *

def obtener_items(usuario):
    lista_items = list()
    
    query_select_muebles = "SELECT * FROM mueble LEFT JOIN ((SELECT * FROM calificación WHERE calificación.correo_usuario = \"%s\") AS tabla_calificacion) ON mueble.referencia = tabla_calificacion.referencia_mueble WHERE mueble.estado = 1" % (usuario)
    lista_muebles_db = ejecutar_consulta(query_select_muebles)
    
    for (referencia, categoria, precio, peso, ancho, alto, fondo, urls, observaciones, estado, referencia_calificacion, usuario_calificacion, calificacion) in lista_muebles_db:
        mueble = {
            "referencia": referencia,
            "categoria": categoria, 
            "precio": precio, 
            "peso": peso, 
            "ancho": ancho, 
            "alto": alto,
            "fondo": fondo,
            "urls": urls.split(), 
            "observaciones": observaciones, 
            "calificacion": calificacion
        }
    
        lista_items.append(mueble)
    
    return lista_items
        
def registrar_calificacion(usuario, referencia_mueble, calificacion):
    query_calificacion = "SELECT * FROM calificación WHERE correo_usuario=\"%s\" AND referencia_mueble=\"%s\"" % (usuario, referencia_mueble)
    lista_resultados = ejecutar_consulta(query_calificacion)
    
    if len(lista_resultados) == 0:
        query_insercion = "INSERT INTO calificación(referencia_mueble, correo_usuario, puntaje) VALUES(%s, %s, %s)"
        datos = (referencia_mueble, usuario, calificacion)
        ejecutar_insercion(query_insercion, datos)
    else:
        query_insercion = "UPDATE calificación SET puntaje=%s WHERE correo_usuario=%s AND referencia_mueble=%s"
        datos = (calificacion, usuario, referencia_mueble)
        ejecutar_actualizacion(query_insercion, datos)
        