from conexion import *
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

def obtener_muebles_df(usuario):
    result = pd.read_sql("SELECT * FROM mueble LEFT JOIN ((SELECT * FROM calificación WHERE calificación.correo_usuario = \"%s\") AS tabla_calificacion) ON mueble.referencia = tabla_calificacion.referencia_mueble" % (usuario), conexion_db)
    return result

def normalizar(fila, columna, minimo, maximo):
    nuevo = (fila[columna] - minimo) / float(maximo - minimo)
    return nuevo

def calcular_distancia(fila, perfil_usuario):
    return np.linalg.norm(fila - perfil_usuario)

def recomendar_contenido(usuario):
    
    muebles_df = obtener_muebles_df(usuario)
    categorias_df = pd.DataFrame(muebles_df["categoria"])
    
    encoder = OneHotEncoder(handle_unknown="ignore")
    encoder.fit(categorias_df)
    
    encoding_categorias = pd.DataFrame(encoder.transform(categorias_df).toarray(), columns = encoder.categories_[0])
    datos = muebles_df.join(encoding_categorias).drop(
            ["categoria", "referencia", "observaciones", "urls", "estado", "correo_usuario", "referencia_mueble"],
            axis=1
    )
    
    datos_calificados = datos.dropna()
    
    calificaciones = pd.DataFrame.transpose(pd.DataFrame(datos_calificados["puntaje"]))
    sumatoria_calificaciones = np.sum(calificaciones, axis=1)

    perfil_usuario = calificaciones.dot(datos_calificados).drop("puntaje", axis=1)
    
    perfil_usuario_ponderado = (1 / sumatoria_calificaciones).dot(perfil_usuario)
    
    perfil_usuario_ponderado["precio"] = (perfil_usuario_ponderado["precio"] - np.min(datos["precio"])) / (np.max(datos["precio"]) - np.min(datos["precio"]))
    perfil_usuario_ponderado["peso"] = (perfil_usuario_ponderado["peso"] - np.min(datos["peso"])) / (np.max(datos["peso"]) - np.min(datos["peso"]))
    perfil_usuario_ponderado["ancho"] = (perfil_usuario_ponderado["ancho"] - np.min(datos["ancho"])) / (np.max(datos["ancho"]) - np.min(datos["ancho"]))
    perfil_usuario_ponderado["alto"] = (perfil_usuario_ponderado["alto"] - np.min(datos["alto"])) / (np.max(datos["alto"]) - np.min(datos["alto"]))
    perfil_usuario_ponderado["profundo"] = (perfil_usuario_ponderado["profundo"] - np.min(datos["profundo"])) / (np.max(datos["profundo"]) - np.min(datos["profundo"]))
    
    datos_no_calificados = datos[datos.isnull().any(axis=1)].drop("puntaje", axis=1)
    
    datos_no_calificados['precio'] = datos_no_calificados.apply(
            normalizar, 
            axis=1, 
            args=["precio", np.min(datos["precio"]), np.max(datos["precio"])]
    )
    
    datos_no_calificados['peso'] = datos_no_calificados.apply(
            normalizar, 
            axis=1, 
            args=["peso", np.min(datos["peso"]), np.max(datos["peso"])]
    )
    
    datos_no_calificados['ancho'] = datos_no_calificados.apply(
            normalizar, 
            axis=1, 
            args=["ancho", np.min(datos["ancho"]), np.max(datos["ancho"])]
    )
    
    datos_no_calificados['alto'] = datos_no_calificados.apply(
            normalizar, 
            axis=1, 
            args=["alto", np.min(datos["alto"]), np.max(datos["alto"])]
    )
    
    datos_no_calificados['profundo'] = datos_no_calificados.apply(
            normalizar, 
            axis=1, 
            args=["profundo", np.min(datos["profundo"]), np.max(datos["profundo"])]
    )

    datos_no_calificados['distancia'] = datos_no_calificados.apply(calcular_distancia, axis=1, args=[perfil_usuario_ponderado])    
    
    return datos_no_calificados.join(muebles_df["referencia"])[["referencia", "distancia"]]
    