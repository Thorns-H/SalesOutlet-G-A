"""
Sales Outlet - using Tkinter for GUI

Abraham Magaña Hernández & Gerardo Gabriel Mercado Guerra

We're not familirized with mySQL or SQLite so, we're trying to make this work first just using code,
we plan on using a data base tho.

Images Right's = Abraham Magaña Hernández @ Thorns
"""
# Library's (time,datetime,random and even sqlite3 are not in use right now, but they'll so don't mind that)
from tkinter import *
from tkinter import ttk
import time
import datetime
import random
import sqlite3
# Delete Variable it's so important, you need to put this on every function to clear labels and change it's value if the windows closes, super important!
delete=bool(False)

# This Function clears any Labels
def clear(function):
    global delete
    function.destroy()
    delete=False

# This Function it's the login one, you need to log in before using the programa obviously (Of course i am planning on using data base for this)
def login():
    global loginVerify, delete
    user=textBoxlogin.get()
    password=textBoxpassword.get()
    if user in ["Abraham","Thorns"] and password in ["123"]:
        if delete==False:
            pass
        else:
            clear(loginVerify)
        loginSuccess="¡Bienvenido de vuelta "+user+"!"
        loginVerify=Label(window,text=loginSuccess,font=("Calibri",10),fg="green3")
        loginVerify.pack()
        delete=True
        mainWindow()
    else:
        if user in [""] and password in [""]:
            if delete==False:
                pass
            else:
                clear(loginVerify)
            error="¡Necesita ingresar un usuario y contraseña!"
            delete=True
        elif user!="" and password!="":
            if delete==False:
                pass
            else:
                clear(loginVerify)
            error="Usuario o Contraseña Incorrectos!"
            delete=True 
        else:
            if delete==False:
                pass
            else:
                clear(loginVerify)
            error="¡Falta ingresar algún tipo de dato!"
            delete=True
        loginVerify=Label(window,text=error,font=("Calibri",10),fg="red")
        loginVerify.pack()

# This Function "Registers" the Product Input, here it's where the database is missing for now
def register():
    global mainWindow,IDTextBox,delete,productAdd,productTable,productPrice
    productType=IDTextBox.get()
    productType=productType.lower()
    productType=productType.title()
    if productType in ["Roles","Capuchino","Moka","Flat White","Latte","Chai","Dirty Chai","Chocolate","Golden Milk", "Taro",
    "Cajeta","Cacao","Ice Latte","Panque","Brownie","Americano G","Soda Italiana S"]:
        if delete==False:
            pass
        else:
            clear(productAdd)
        productAdd=Label(mainWindow,text=f'¡Producto "{productType}" Agregado!',font=("Calibri",10),fg="green3")
        productAdd.pack()
        productPrice=35
        totalPrice=totalPrice+productPrice
        productTable.insert("",0,text=productType,values=(f"${productPrice}"))
        delete=True
    elif productType in ["Frape Chocolate","Frape Café","Frape Cafe","Frape Cajeta","Frape Vainilla","Frape Oreo","Frape Taro","FrapeMazapan",
    "Frape Moka","Cold Brew","Soda Italiana","Tisana","Dirty Chai G"]:
        if delete==False:
            pass
        else:
            clear(productAdd)
        productAdd=Label(mainWindow,text=f'¡Producto "{productType}" Agregado!',font=("Calibri",10),fg="green3")
        productAdd.pack()
        productPrice=40
        totalPrice=totalPrice+productPrice
        productTable.insert("",0,text=productType,values=(f"${productPrice}"))
        delete=True
    elif productType in ["Doble","Cortado","Cortado Doble","Refrescos","Leche Santa Clara","Galletas Chispas","Lungo"]:
        if delete==False:
            pass
        else:
            clear(productAdd)
        productAdd=Label(mainWindow,text=f'¡Producto "{productType}" Agregado!',font=("Calibri",10),fg="green3")
        productAdd.pack()
        productPrice=20
        totalPrice=totalPrice+productPrice
        productTable.insert("",0,text=productType,values=(f"${productPrice}"))
        delete=True
    elif productType in ["Malteada Chocolate","Malteada Vainilla","Malteada Fresa","Brownie Con Nieve","Brownie Nieve"]:
        if delete==False:
            pass
        else:
            clear(productAdd)
        productAdd=Label(mainWindow,text=f'¡Producto "{productType}" Agregado!',font=("Calibri",10),fg="green3")
        productAdd.pack()
        productPrice=55
        totalPrice=totalPrice+productPrice
        productTable.insert("",0,text=productType,values=(f"${productPrice}"))
        delete=True
    elif productType in ["Espreso","Galletas Ketto"]:
        if delete==False:
            pass
        else:
            clear(productAdd)
        productAdd=Label(mainWindow,text=f'¡Producto "{productType}" Agregado!',font=("Calibri",10),fg="green3")
        productAdd.pack()
        productPrice=15
        totalPrice=totalPrice+productPrice
        productTable.insert("",0,text=productType,values=(f"${productPrice}"))
        delete=True
    elif productType in ["Americano","Lungo G"]:
        if delete==False:
            pass
        else:
            clear(productAdd)
        productAdd=Label(mainWindow,text=f'¡Producto "{productType}" Agregado!',font=("Calibri",10),fg="green3")
        productAdd.pack()
        productPrice=25
        totalPrice=totalPrice+productPrice
        productTable.insert("",0,text=productType,values=(f"${productPrice}"))
        delete=True
    elif productType in ["Te Snapple","Mini Panque"]:
        if delete==False:
            pass
        else:
            clear(productAdd)
        productAdd=Label(mainWindow,text=f'¡Producto "{productType}" Agregado!',font=("Calibri",10),fg="green3")
        productAdd.pack()
        productPrice=18
        totalPrice=totalPrice+productPrice
        productTable.insert("",0,text=productType,values=(f"${productPrice}"))
        delete=True
    elif productType in ["Panini Jamon","Panini Jamón","Panini Jamón Pavo","Panini Jamon Pavo","Café 1/4","Cafe 1/4"]:
        if delete==False:
            pass
        else:
            clear(productAdd)
        productAdd=Label(mainWindow,text=f'¡Producto "{productType}" Agregado!',font=("Calibri",10),fg="green3")
        productAdd.pack()
        productPrice=65
        totalPrice=totalPrice+productPrice
        productTable.insert("",0,text=productType,values=(f"${productPrice}"))
        delete=True
    elif productType in ["Panini Selva Negra"]:
        if delete==False:
            pass
        else:
            clear(productAdd)
        productAdd=Label(mainWindow,text=f'¡Producto "{productType}" Agregado!',font=("Calibri",10),fg="green3")
        productAdd.pack()
        productPrice=85
        totalPrice=totalPrice+productPrice
        productTable.insert("",0,text=productType,values=(f"${productPrice}"))
        delete=True
    elif productType in ["Te Frio","Té Frio","Té","Te","Capuchino M","Moka M","Flat White M","Latte M","Chai M","Chocolate M"]:
        if delete==False:
            pass
        else:
            clear(productAdd)
        productAdd=Label(mainWindow,text=f'¡Producto "{productType}" Agregado!',font=("Calibri",10),fg="green3")
        productAdd.pack()
        productPrice=30
        totalPrice=totalPrice+productPrice
        productTable.insert("",0,text=productType,values=(f"${productPrice}"))
        delete=True
    elif productType in ["Adiccion","Chocoqueso","Pastel Zanahoria","Muss Guayaba","Muss Frutos",
    "Muss limon","Strudell","Corazon De Leon","Gansio Ketto","Pinguino Ketto","Chescake Brownie",
    "Chescake fresa","Beso De Chocolate","Crunch De Menta","Domo Mazapan","Trufa","Tarta De Frutas"]:
        if delete==False:
            pass
        else:
            clear(productAdd)
        productAdd=Label(mainWindow,text=f'¡Producto "{productType}" Agregado!',font=("Calibri",10),fg="green3")
        productAdd.pack()
        productPrice=60
        totalPrice=totalPrice+productPrice
        productTable.insert("",0,text=productType,values=(f"${productPrice}"))
        delete=True
    elif productType in ["Golden Milk G","Frape Especial"]:
        if delete==False:
            pass
        else:
            clear(productAdd)
        productAdd=Label(mainWindow,text=f'¡Producto "{productType}" Agregado!',font=("Calibri",10),fg="green3")
        productAdd.pack()
        productPrice=45
        totalPrice=totalPrice+productPrice
        productTable.insert("",0,text=productType,values=(f"${productPrice}"))
        delete=True
    elif productType in ["Café 1kg","Cafe 1kg"]:
        if delete==False:
            pass
        else:
            clear(productAdd)
        productAdd=Label(mainWindow,text=f'¡Producto "{productType}" Agregado!',font=("Calibri",10),fg="green3")
        productAdd.pack()
        productPrice=265
        totalPrice=totalPrice+productPrice
        productTable.insert("",0,text=productType,values=(f"${productPrice}"))
        delete=True
    else:
        if delete==False:
            pass
        else:
            clear(productAdd)
        productAdd=Label(mainWindow,text=f'¡Producto "{productType}" NO EXISTE!',font=("Calibri",10),fg="red2")
        productAdd.pack()
        delete=True

# This Function it's my main window, not the root one, that's called "window"    
def mainWindow():
    global mainWindow,imageLogo,IDTextBox,delete,productTable
    delete=False
    window.destroy()
    mainWindow=Tk()
    mainWindow.resizable(1,1)
    mainWindow.iconbitmap("titleIcon.ico")
    mainWindow.geometry("430x470")
    mainWindow.title("Café DiFiore - Administrador")

    imageLogo=PhotoImage(file="logoImage.gif")
    topLabel=Label(image=imageLogo)
    topLabel.pack()
    productTable=ttk.Treeview(mainWindow,columns=("#1",))
    productTable.heading("#0",text="     Nombre",anchor=W)
    productTable.heading("#1",text="     Precio",anchor=W)
    productTable.pack()

    titleLabel=Label(mainWindow, text="Ingrese el Tipo de Producto :", font=("Calibri",15))
    titleLabel.pack()
    IDTextBox=Entry(mainWindow,font=("Calibri",12))
    IDTextBox.pack(pady=2)
    checkButton=Button(mainWindow,text="Aceptar",font=("Calibri",10),command=register)
    checkButton.pack(pady=4)

# Root Window - Before Login Function
window=Tk()
window.resizable(0,0)
window.iconbitmap("titleIcon.ico")
window.geometry("400x320")
window.title("Login - Café DiFiore")

emptyLabel=Label(window, text="\n",font=("Calibri",5))
emptyLabel.pack()
imageLogin=PhotoImage(file="loginImage.gif")
imageLabel=Label(window,image=imageLogin)
imageLabel.pack()
loginLabel=Label(window, text="Usuario :",font=(None, 15))
loginLabel.pack()
textBoxlogin=Entry(window,font=("Helvetica",12))
textBoxlogin.focus()
textBoxlogin.pack()

passwordLabel=Label(window, text="Contraseña :",font=(None, 15))
passwordLabel.pack()
textBoxpassword=Entry(window,show="*",font=("Helvetica",12))
textBoxpassword.pack()

emptyLabel2=Label(window, text="\n",font=("Calibri",2))
emptyLabel2.pack()
bottom1=Button(window, text="Login", command=login)
bottom1.pack()

# Exec
window.mainloop()