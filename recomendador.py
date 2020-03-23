from colaborativo import *
from contenido import *
from conexion import *

def integrar_recomendaciones(fila):   
    ponderacion_colaborativo = 0.8
    ponderacion_contenido = 0.2
    
    calificacion_contenido = 10 / (fila["distancia"] + 1)
    
    return ponderacion_colaborativo * fila["calificacion"] + ponderacion_contenido * calificacion_contenido

def hay_calificaciones(usuario):
    query_verificacion = "SELECT * FROM calificación WHERE correo_usuario=\"%s\"" % (usuario)
    resultado = ejecutar_consulta(query_verificacion)
    if len(resultado) == 0:
        return False
    else:
        return True
    
def obtener_muebles_preferidos(usuario):
    query_verificacion = "SELECT referencia, 6 as recomendacion_hibrida FROM usuario, mueble WHERE correo=\"%s\" AND preferencia = categoria AND estado = 1" % (usuario)
    return pd.read_sql(query_verificacion, conexion_db)
        
def recomendar(usuario):
    if hay_calificaciones(usuario):    
        recomendacion_colaborativa = recomendar_colaborativo(usuario)
        recomendacion_contenido = recomendar_contenido(usuario)
    
        recomendacion = recomendacion_colaborativa.join(recomendacion_contenido.set_index("referencia"), on="referencia")
        recomendacion["recomendacion_hibrida"] = recomendacion.apply(integrar_recomendaciones, axis=1)
      
        recomendacion = recomendacion.sort_values(by="recomendacion_hibrida", ascending=False)
    
        return recomendacion.head(n=10)
    else:
        return obtener_muebles_preferidos(usuario).head(n=10)


