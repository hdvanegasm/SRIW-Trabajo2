from conexion import *
from surprise import Dataset
from surprise import Reader
from surprise import SVD


def obtener_calificaciones():
    result = pd.read_sql("SELECT * FROM calificación", conexion_db)
    return result

def obtener_muebles_no_calificados(usuario):
    result = pd.read_sql("SELECT * FROM mueble LEFT JOIN ((SELECT * FROM calificación WHERE calificación.correo_usuario = \"%s\") AS tabla_calificacion) ON mueble.referencia = tabla_calificacion.referencia_mueble WHERE estado=1" % (usuario), conexion_db)
    return result[result.isnull().any(axis=1)]["referencia"]

def predecir(fila, usuario, modelo):
    prediccion = modelo.predict(usuario, fila["referencia"])
    return prediccion.est


def recomendar_colaborativo(usuario):
    datos_df = obtener_calificaciones()
    reader = Reader(rating_scale=(1, 10))
    
    datos = Dataset.load_from_df(datos_df[["correo_usuario", "referencia_mueble", "puntaje"]], reader)
    
    referencias_prediccion = pd.DataFrame.to_numpy(obtener_muebles_no_calificados(usuario))

    training_dataset = datos.build_full_trainset()
    
    svd = SVD()
    svd.fit(training_dataset)
    
    resultado = pd.DataFrame(referencias_prediccion, columns=["referencia"])
    resultado["calificacion"] = resultado.apply(predecir, axis=1, args=[usuario, svd])
    
    return resultado