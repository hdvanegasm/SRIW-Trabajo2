from tkinter import *
from conexion import *

##################################### UTILS ############################################
def checkIfNull(email, name, password, rpassword):
    return email != '' and name != '' and password != '' and rpassword != ''

def checkPass(pass1, pass2):
    return pass1 == pass2

def insertUser(emailValue, nameValue, passValue):
    query = ("INSERT INTO usuario "
            "(correo, nombre, contrasena) "
            "VALUES (%s, %s, %s)")
    data = (emailValue, nameValue, passValue)
    ejecutar_insercion(query, data)

def clearData():
    email.delete(0, END)
    name.delete(0, END)
    password.delete(0, END)
    rpassword.delete(0, END)

##################################### REGISTER SECTION ############################################
def registro():
    emailValue = email.get().strip()
    nameValue = name.get()
    passValue = password.get()
    rpassValue = rpassword.get()

    if (checkIfNull(emailValue, nameValue, passValue, rpassValue) and checkPass(passValue, rpassValue)):
        insertUser(emailValue, nameValue, passValue)
        clearData()

    else : 
        print('Falta data')

##################################### LOGIN SECTION ############################################
def irALogin():
    registerScreen.destroy()

##################################### DESIGN SECTION ############################################

def initRegistration(parent):
    global registerScreen
    global email
    global name
    global password
    global rpassword

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

    # Login section
    login = Button(registerScreen, text='Ir a login', command=irALogin)
    login.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")

    # Register section
    register = Button(registerScreen, text='Register', command=registro)
    register.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

    registerScreen.grid_columnconfigure(0,weight=1)
    registerScreen.grid_columnconfigure(1,weight=1)