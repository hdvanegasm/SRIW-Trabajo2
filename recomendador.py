from colaborativo import *
from contenido import *

def integrar_recomendaciones(fila):
    ponderacion_colaborativo = 0.8
    ponderacion_contenido = 0.2
    
    calificacion_contenido = 10 / (fila["distancia"] + 1)
    
    return ponderacion_colaborativo * fila["calificacion"] + ponderacion_contenido * calificacion_contenido

def recomendar(usuario):
    recomendacion_colaborativa = recomendar_colaborativo(usuario)
    recomendacion_contenido = recomendar_contenido(usuario)

    recomendacion = recomendacion_colaborativa.join(recomendacion_contenido.set_index("referencia"), on="referencia")
    recomendacion["recomendacion_hibrida"] = recomendacion.apply(integrar_recomendaciones, axis=1)
  
    return recomendacion

