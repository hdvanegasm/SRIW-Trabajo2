from tkinter import *
from conexion import *
from registro import *
from home import *

##################################### UTILS ############################################
def checkIfNull(email, password):
    return email != '' and password != ''

def checkIfUserExist(email, password):
    query = ("SELECT correo, contrasena FROM usuario "
            "WHERE correo='" + email + "' AND contrasena='" + password +"'")  
    return len(ejecutar_consulta(query))


def clearData():
    email.delete(0, END)
    password.delete(0, END)

##################################### LOGIN SECTION ############################################
def login():
    emailValue = email.get().strip()
    passValue = password.get()

    if (checkIfNull(emailValue, passValue) and checkIfUserExist(emailValue, passValue)):
        clearData()
        initHome(screen, emailValue)
        screen.withdraw()

##################################### REGISTER SECTION ############################################
def register():
    initRegistration(screen)

##################################### DESIGN SECTION ############################################
screen = Tk()
screen.title('Login')

pageLabel = Label(screen, text='Login')
pageLabel.grid(row=0, columnspan=2)

emailLabel = Label(screen, text='Email')
emailLabel.grid(row=1, column=0, sticky=W)
email = Entry(screen)
email.grid(row=1, column=1, padx=5, pady=5)

passwordLabel = Label(screen, text='Password')
passwordLabel.grid(row=2, column=0, sticky=W)
password = Entry(screen, show="*")
password.grid(row=2, column=1, padx=5, pady=5)

login = Button(screen, text='Login', command=login)
login.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

register = Button(screen, text='Register', command=register)
register.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

screen.grid_columnconfigure(0,weight=1)
screen.grid_columnconfigure(1,weight=1)


screen.mainloop()