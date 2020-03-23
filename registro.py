from tkinter import *
from tkinter import ttk
from conexion import *

def initRegistration(parent):
    global registerScreen
    global email
    global name
    global password
    global rpassword

    ##################################### UTILS ############################################
    def checkIfNull(email, name, password, rpassword, preferencia):
        return email != '' and name != '' and password != '' and rpassword != '' and preferencia != ''

    def checkPass(pass1, pass2):
        return pass1 == pass2

    def insertUser(emailValue, nameValue, passValue, preferenciaValue):
        query = ("INSERT INTO usuario "
                "(correo, nombre, contrasena, preferencia) "
                "VALUES (%s, %s, %s, %s)")
        data = (emailValue, nameValue, passValue, preferenciaValue)
        ejecutar_insercion(query, data)
        
    ################################ METODO NUEVO PARA OBTENER LAS CATEGORIAS ###################
    def getCategories():
        query = "SELECT DISTINCT categoria FROM mueble"
        resultados = ejecutar_consulta(query)
        
        lista_categorias = list()
        
        for (elemento, ) in resultados:
            lista_categorias.append(elemento)
            
        return lista_categorias
    ################################################################################################
    
    def clearData():
        email.delete(0, END)
        name.delete(0, END)
        password.delete(0, END)
        rpassword.delete(0, END)
        preferencia.delete(0, END)

    ##################################### REGISTER SECTION ############################################
    def registro():
        emailValue = email.get().strip()
        nameValue = name.get()
        passValue = password.get()
        rpassValue = rpassword.get()
        preferenciaValue = preferencia.get()

        if (checkIfNull(emailValue, nameValue, passValue, rpassValue, preferencia) and checkPass(passValue, rpassValue)):
            insertUser(emailValue, nameValue, passValue, preferenciaValue)
            clearData()

        else : 
            print('Falta información')

    ##################################### LOGIN SECTION ############################################
    def irALogin():
        registerScreen.destroy()



    ##################################### DESIGN SECTION ############################################
    registerScreen = Toplevel(parent)
    registerScreen.title('Registro')

    pageLabel = Label(registerScreen, text='Registro')
    pageLabel.grid(row=0, columnspan=2)

    emailLabel = Label(registerScreen, text='Email')
    emailLabel.grid(row=1, column=0, sticky=W)
    email = Entry(registerScreen)
    email.grid(row=1, column=1, padx=5, pady=5)

    nameLabel = Label(registerScreen, text='Name')
    nameLabel.grid(row=2, column=0, sticky=W)
    name = Entry(registerScreen)
    name.grid(row=2, column=1, padx=5, pady=5)

    passwordLabel = Label(registerScreen, text='Password')
    passwordLabel.grid(row=3, column=0, sticky=W)
    password = Entry(registerScreen, show="*")
    password.grid(row=3, column=1, padx=5, pady=5)

    rpasswordLabel = Label(registerScreen,text='Repetir Password')
    rpasswordLabel.grid(row=4, column=0, sticky=W)
    rpassword = Entry(registerScreen, show="*")
    rpassword.grid(row=4, column=1, padx=5, pady=5)
    
    preferenciaLabel = Label(registerScreen,text='Preferencia')
    preferenciaLabel.grid(row=5, column=0, sticky=W)
    preferencia = ttk.Combobox(registerScreen, values=getCategories())
    preferencia.grid(row=5, column=1, padx=5, pady=5)

    # Login section
    login = Button(registerScreen, text='Ir a login', command=irALogin)
    login.grid(row=6, column=1, padx=5, pady=5, sticky="nsew")

    # Register section
    register = Button(registerScreen, text='Register', command=registro)
    register.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")

    registerScreen.grid_columnconfigure(0,weight=1)
    registerScreen.grid_columnconfigure(1,weight=1)
    