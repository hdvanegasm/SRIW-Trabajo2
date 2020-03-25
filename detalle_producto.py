from tkinter import *
from explorador import *
from modelo import *
from conexion import *
import webbrowser
from objects_list import *
from evaluacion import *
from recomendador import *

aciertoXY = 0

def aciertoX(acierto):
    global aciertoXY 
    if(acierto == 1 ):
        aciertoXY = 1
    else:
        aciertoXY = 0
    return True
    
def initDetails(parent, item,email):
    
    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox('all'))
    def openweb(url):
        webbrowser.open_new(url)

    def checkRating(rating,referencia):
        global aciertoXY 
        df = recomendar(email)
        if aciertoXY == 1:
            aux = (df.loc[df['referencia'] == item['referencia']])['recomendacion_hibrida'].values[0]
            registrar_acierto(email, int(rating.get()), int(aux))
        
        aciertoXY = 0
        
        if 1 <= (int(rating.get())) and (int(rating.get())) <= 10:
            query = ("INSERT INTO calificación "
                     "(referencia_mueble, correo_usuario, puntaje) "
                     "VALUES (%s, %s, %s)"
                     "ON DUPLICATE KEY UPDATE "
                     "puntaje = " +rating.get())
            data = (referencia, email, rating.get())
            ejecutar_insercion(query, data)
            Label(detailsFrame, text='Calificación registrada').grid(row=i + 4, column=0)
            return True
        else:
            Label(detailsFrame, text='El valor debe ser entre 1 y 10').grid(row=i + 4, column=0)
            rating.delete(0, END)
            return False

    
    detailScreen = Toplevel(parent)
    detailScreen.title('Detalles producto')

    canvas = Canvas(detailScreen, width=800, height=400)
    canvas.configure()
    canvas.grid(row=0, column=0)

    detailsFrame = Frame(canvas)
    canvas.create_window((0, 0), window=detailsFrame, anchor='nw')

    scrollbar = Scrollbar(detailScreen, orient="vertical", command=canvas.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")

    scrollbarX = Scrollbar(detailScreen, orient="horizontal", command=canvas.xview)
    scrollbarX.grid(row=1, column=0, sticky="ew")

    canvas.configure(yscrollcommand=scrollbar.set, xscrollcommand=scrollbarX.set)
    canvas.bind('<Configure>', on_configure)

    Label(detailsFrame, text='Observaciones').grid(row=0, column=0)
    Label(detailsFrame, text=item['observaciones']).grid(row=1, column=0)

    Label(detailsFrame, text='Links del producto').grid(row=2, column=0)
    i = 3
    item['urls']
    btn1 = Button(detailsFrame, text=item['urls'][0], command=lambda:openweb(item['urls'][0])).grid(row=i, column=0)
    if len(item['urls']) > 1:
        i += 1
        btn2 = Button(detailsFrame, text=item['urls'][1], command=lambda:openweb(item['urls'][1])).grid(row=i, column=0)

    Label(detailsFrame, text='\n Ingresar una calificación al producto( de 1 a 10):').grid(row=i+1, column=0)
    rating = Entry(detailsFrame,justify=CENTER)
    rating.grid(row=i+2, column=0)
    Button(detailsFrame, text='Enviar', command=lambda: checkRating(rating,item['referencia'])).grid(row=i+3, column=0)

