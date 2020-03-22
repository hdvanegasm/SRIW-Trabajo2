from tkinter import *
from explorador import *
from modelo import *

def initHome(parent, email):
    homeScreen = Toplevel(parent)
    homeScreen.title('Lista de muebles')

    objectsList = []
    objectsList.append(Mueble(1,2,122222, 3, 4, 5, 6, 'holi', 1, 'https://google.com'))
    objectsList.append(Mueble(1,2,122222, 3, 4, 5, 6, 'holi', 1, 'https://google.com'))
    objectsList.append(Mueble(1,2,122222, 3, 4, 5, 6, 'holi', 1, 'https://google.com'))


    ##################################### UTILS ############################################
    def showItem(itemsFrame, item, i):
        Label(itemsFrame, text=item['referencia']).grid(row=i, column=0)
        Label(itemsFrame, text=item['categoria']).grid(row=i, column=1)
        Label(itemsFrame, text=item['precio']).grid(row=i, column=2)
        Label(itemsFrame, text=item['peso']).grid(row=i, column=3)
        Label(itemsFrame, text=item['ancho']).grid(row=i, column=4)
        Label(itemsFrame, text=item['alto']).grid(row=i, column=5)
        Label(itemsFrame, text=item['fondo']).grid(row=i, column=6)
        Label(itemsFrame, text=item['calificacion']).grid(row=i, column=7)
        Button(itemsFrame, text='Ver mas').grid(row=i, column=8)
    
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

    ##################################### LOGOUT SECTION ############################################
    def logout():
        parent.update()
        parent.deiconify()
        homeScreen.destroy()

    ##################################### DESIGN SECTION ############################################

    i = 1
    itemsFrame = Frame(homeScreen)
    showHeader(itemsFrame)
    for item in obtener_items(email):
        showItem(itemsFrame, item, i)
        i+=1
    itemsFrame.pack(fill='x')

    Button(homeScreen, text='Salir', command=logout).pack()
