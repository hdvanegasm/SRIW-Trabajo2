from tkinter import *
from tkinter import messagebox
from explorador import *
from modelo import *
from detalle_producto import *
from recomendador import *
from evaluacion import *

def initHome(parent, email):
    homeScreen = Toplevel(parent)
    homeScreen.title('Lista de muebles')

    ##################################### UTILS ############################################
    def showMore(parent, item):
        initDetails(parent, item,email)

    def showItem(itemsFrame, item, i):
        Label(itemsFrame, text=item['referencia']).grid(row=i, column=0)
        Label(itemsFrame, text=item['categoria']).grid(row=i, column=1)
        Label(itemsFrame, text=item['precio']).grid(row=i, column=2)
        Label(itemsFrame, text=item['peso']).grid(row=i, column=3)
        Label(itemsFrame, text=item['ancho']).grid(row=i, column=4)
        Label(itemsFrame, text=item['alto']).grid(row=i, column=5)
        Label(itemsFrame, text=item['fondo']).grid(row=i, column=6)
        Label(itemsFrame, text=item['calificacion']).grid(row=i, column=7)
        Button(itemsFrame, text='Ver mas', command=lambda: showMore(itemsFrame, item)).grid(row=i, column=8)

    def showHeader(itemsFrame):
        Label(itemsFrame, text='Referencia').grid(row=0, column=0)
        Label(itemsFrame, text='Categoria').grid(row=0, column=1)
        Label(itemsFrame, text='Precio').grid(row=0, column=2)
        Label(itemsFrame, text='Peso').grid(row=0, column=3)
        Label(itemsFrame, text='Ancho').grid(row=0, column=4)
        Label(itemsFrame, text='Alto').grid(row=0, column=5)
        Label(itemsFrame, text='Fondo').grid(row=0, column=6)
        Label(itemsFrame, text='Calificacion').grid(row=0, column=7)
        Label(itemsFrame, text='Acción').grid(row=0, column=8)
    
    def showHeader2(itemsFrame):
        Label(itemsFrame, text='Referencia').grid(row=0, column=0)
        Label(itemsFrame, text='Categoria').grid(row=0, column=1)
        Label(itemsFrame, text='Precio').grid(row=0, column=2)
        Label(itemsFrame, text='Peso').grid(row=0, column=3)
        Label(itemsFrame, text='Ancho').grid(row=0, column=4)
        Label(itemsFrame, text='Alto').grid(row=0, column=5)
        Label(itemsFrame, text='Fondo').grid(row=0, column=6)
        Label(itemsFrame, text='Acción').grid(row=0, column=8)
        
    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox('all'))

    ##################################### LOGOUT SECTION ############################################
    def logout():
        parent.update()
        parent.deiconify()
        homeScreen.destroy()

    ##################################### RECOMMENDATION ############################################
    def recomendaciones():
        

        df = recomendar(email)
        aciertoX(1, df)
        for items2 in itemsFrame.winfo_children():
            items2.destroy()
            
        showHeader2(itemsFrame)
        i = 1
        for item in obtener_items(email):
            for referencia in df['referencia']:
                if (item['referencia'] == referencia):
                    showItem(itemsFrame, item , i)
                    i+=1
        
                    
    def desempeno():
        aux = obtener_desempeno(email)
        window = Tk()
        window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
        window.withdraw()
        messagebox.showinfo('Desempeño Recomendacion', aux)
        window.deiconify()
        window.destroy()
        
    def atras():
        aciertoX(0,0)
        i = 1
        showHeader(itemsFrame)
        for item in obtener_items(email):
            showItem(itemsFrame, item, i)
            i+=1
        
        Button(homeScreen, text='Salir', command=logout).grid(row=5, column=0)
        Button(homeScreen, text='Recomendar', command= recomendaciones).grid(row=2, column=0)
        Button(homeScreen, text='Obtener Desempeño', command= desempeno).grid(row=3, column=0)
        Button(homeScreen, text='Atras', command= atras).grid(row=4, column=0)
        
    ##################################### DESIGN SECTION ############################################          
    i = 1
    
    canvas = Canvas(homeScreen, width=600, height=600)
    canvas.configure()
    canvas.grid(row=0, column=0)

    scrollbar = Scrollbar(homeScreen, orient="vertical", command=canvas.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")

    scrollbarX = Scrollbar(homeScreen, orient="horizontal", command=canvas.xview)
    scrollbarX.grid(row=1, column=0, sticky="ew")

    canvas.configure(yscrollcommand = scrollbar.set, xscrollcommand = scrollbarX.set)
    canvas.bind('<Configure>', on_configure)

    itemsFrame = Frame(canvas)
    canvas.create_window((0,0), window=itemsFrame, anchor='nw')

    showHeader(itemsFrame)
    for item in obtener_items(email):
        showItem(itemsFrame, item, i)
        i+=1
    
    Button(homeScreen, text='Salir', command=logout).grid(row=5, column=0)
    Button(homeScreen, text='Recomendar', command= recomendaciones).grid(row=2, column=0)
    Button(homeScreen, text='Obtener Desempeño', command= desempeno).grid(row=3, column=0)
    Button(homeScreen, text='Atras', command= atras).grid(row=4, column=0)
    
    
    ##################################### BOTON RECOMENDAR ############################################


            
            
    
    
    
    
    