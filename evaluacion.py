
from conexion import *

def verificar_acierto(usuario):
    query = "SELECT * FROM acierto WHERE correo_usuario=\"%s\"" % (usuario)
    resultado = ejecutar_consulta(query)
    if len(resultado) == 0:
        query_insercion = "INSERT INTO acierto(correo_usuario, numero_aciertos, total_valoraciones) VALUES (%s, 0, 0)"
        data = (usuario, )
        ejecutar_insercion(query_insercion, data)

def actualizar_acierto(usuario, acierto):
    if acierto:
        query = "UPDATE acierto SET numero_aciertos=numero_aciertos+1, total_valoraciones=total_valoraciones+1 WHERE correo_usuario=%s"
        data = (usuario, )
        ejecutar_actualizacion(query, data)
    else:
        query = "UPDATE acierto SET total_valoraciones=total_valoraciones+1 WHERE correo_usuario=%s"
        data = (usuario, )
        ejecutar_actualizacion(query, data)
        
def registrar_acierto(usuario, calificacion, recomendacion):
    verificar_acierto(usuario)        
    if abs(calificacion - recomendacion) <= 1.5:
        actualizar_acierto(usuario, acierto=True)
    else:
        actualizar_acierto(usuario, acierto=False)
        
def obtener_desempeno(usuario):
    query = "SELECT 100 * numero_aciertos / total_valoraciones AS desempeno FROM acierto WHERE correo_usuario=\"%s\"" % (usuario)
    resultado = ejecutar_consulta(query)
    if len(resultado) == 0:
        return "No se puede calcular el desempeño"
    else:
        return str(resultado[0][0]) + "%"
