from tkinter import *

def initHome(parent, email):
    homeScreen = Toplevel(parent)
    homeScreen.title('Home')

    ##################################### LOGOUT SECTION ############################################
    def logout():
        parent.update()
        parent.deiconify()
        homeScreen.destroy()

    Button(homeScreen, text='Salir', command=logout).pack()