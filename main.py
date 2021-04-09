"""
Sales Outlet - using Tkinter for GUI
Punto de Venta - usando TKinter para la Interfaz Gráfica

Abraham Magaña Hernández & Gerardo Gabriel Mercado Guerra

This is the first time i've been working with GUI and i really wanted to use a database but i don't have too much time to learn that
im pretty new to this and i make this work using only code and large lists.

La primera vez que trabajo usando interfaces gráficas, realmente queria utilizar una base de datos para este programa, tal vez lo haga
en un futuro, pero por ahora funciona usando listas de los productos.

Abraham Magaña Hernández © 
"""
# Libraries (As i said I only use tkinter and datetime to put the function about the current hour and date to the .txt files output)
# Librerias (Como dije, use Tkinter y pues la libreria datime esta ahí para incluir la función de dar la hora y el día actuales)
from tkinter import *
from tkinter import ttk
import datetime
import random
# Delete Variable it's so important, you need to put this on every function to clear labels and change it's value if the windows closes, super important!
# La Variable "Delete", esta variable es super importante ya que limpia o limita cada cuando se debe limpiar el programa, la encontrarás seguido
delete=bool(False)
gain=int(0)

# This Function clears any Labels
# Esta función limpia algunas Labels, o etiquetas, como le digas, usando la variable delete
def clear(function):
    global delete
    function.destroy()
    delete=False

# This Function it's the login one, you need to log in before using the programa obviously
# Esta es la función de logeo, ingreso, como quieras decirle, necesitas logearte para entrar en el programa
def login():
    global loginVerify, delete, today, user, gain
    user=textBoxlogin.get()
    password=textBoxpassword.get()
    if user in ["Abraham","Thorns"] and password in ["123"]:
        date=datetime.datetime.now()
        today=date.strftime("%d/%m/%Y %H:%M:%S")
        hour=date.strftime("%H")
        file=open("ganancias.txt","w")
        file.write(f"------------------------------------------------------\n")
        file.write(f"Cafe DiFiore - Administracion de Facturaciones Reales\n")
        file.write(f"------------------------------------------------------\n")
        file=open("logs.txt","w")
        file.write(f"-----------------------------------------\n")
        file.write(f"Cafe DiFiore - Administracion de Usuarios \n")
        file.write(f"-----------------------------------------\n")
        if hour in ["8","9","10","11","12","13","14","15","16","17","18","19","20"]:    
            file=open("logs.txt","a")
            file.write(f"{today} - {user} se ha logeado!\n")
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
            if delete==False:
                pass
            else:
                clear(loginVerify)
            loginSuccess=f"¡Ingreso Fuera de Hora de Servicio!"
            loginVerify=Label(window,text=loginSuccess,font=("Calibri",10),fg="red")
            loginVerify.pack()
            delete=True
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

# This Function "Registers" the Product Input
# Esta función registra el producto que entre al programa
def register():
    global mainWindow,IDTextBox,delete,productAdd,productTable,productPrice,gain
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
        gain=gain+productPrice
        productTable.insert("",0,text=productType,values=(f"${productPrice}"))
        date=datetime.datetime.now()
        today=date.strftime("%d/%m/%Y %H:%M:%S")
        file=open("logs.txt","a")
        file.write(f"{today} - {user} ha facturado un {productType} a ${productPrice}\n")
        delete=True
    elif productType in ["Frape Chocolate","Frape Café","Frape Cafe","Frape Cajeta","Frape Vainilla","Frape Oreo","Frape Taro","Frape Mazapan",
    "Frape Moka","Cold Brew","Soda Italiana","Tisana","Dirty Chai G"]:
        if delete==False:
            pass
        else:
            clear(productAdd)
        productAdd=Label(mainWindow,text=f'¡Producto "{productType}" Agregado!',font=("Calibri",10),fg="green3")
        productAdd.pack()
        productPrice=40
        gain=gain+productPrice
        productTable.insert("",0,text=productType,values=(f"${productPrice}"))
        date=datetime.datetime.now()
        today=date.strftime("%d/%m/%Y %H:%M:%S")
        file=open("logs.txt","a")
        file.write(f"{today} - {user} ha facturado un {productType} a ${productPrice}\n")
        delete=True
    elif productType in ["Doble","Cortado","Cortado Doble","Refrescos","Leche Santa Clara","Galletas Chispas","Lungo"]:
        if delete==False:
            pass
        else:
            clear(productAdd)
        productAdd=Label(mainWindow,text=f'¡Producto "{productType}" Agregado!',font=("Calibri",10),fg="green3")
        productAdd.pack()
        productPrice=20
        gain=gain+productPrice
        productTable.insert("",0,text=productType,values=(f"${productPrice}"))
        date=datetime.datetime.now()
        today=date.strftime("%d/%m/%Y %H:%M:%S")
        file=open("logs.txt","a")
        file.write(f"{today} - {user} ha facturado un {productType} a ${productPrice}\n")
        delete=True
    elif productType in ["Malteada Chocolate","Malteada Vainilla","Malteada Fresa","Brownie Con Nieve","Brownie Nieve"]:
        if delete==False:
            pass
        else:
            clear(productAdd)
        productAdd=Label(mainWindow,text=f'¡Producto "{productType}" Agregado!',font=("Calibri",10),fg="green3")
        productAdd.pack()
        productPrice=55
        gain=gain+productPrice
        productTable.insert("",0,text=productType,values=(f"${productPrice}"))
        date=datetime.datetime.now()
        today=date.strftime("%d/%m/%Y %H:%M:%S")
        file=open("logs.txt","a")
        file.write(f"{today} - {user} ha facturado un {productType} a ${productPrice}\n")
        delete=True
    elif productType in ["Espreso","Galletas Ketto"]:
        if delete==False:
            pass
        else:
            clear(productAdd)
        productAdd=Label(mainWindow,text=f'¡Producto "{productType}" Agregado!',font=("Calibri",10),fg="green3")
        productAdd.pack()
        productPrice=15
        gain=gain+productPrice
        productTable.insert("",0,text=productType,values=(f"${productPrice}"))
        date=datetime.datetime.now()
        today=date.strftime("%d/%m/%Y %H:%M:%S")
        file=open("logs.txt","a")
        file.write(f"{today} - {user} ha facturado un {productType} a ${productPrice}\n")
        delete=True
    elif productType in ["Americano","Lungo G"]:
        if delete==False:
            pass
        else:
            clear(productAdd)
        productAdd=Label(mainWindow,text=f'¡Producto "{productType}" Agregado!',font=("Calibri",10),fg="green3")
        productAdd.pack()
        productPrice=25
        gain=gain+productPrice
        productTable.insert("",0,text=productType,values=(f"${productPrice}"))
        date=datetime.datetime.now()
        today=date.strftime("%d/%m/%Y %H:%M:%S")
        file=open("logs.txt","a")
        file.write(f"{today} - {user} ha facturado un {productType} a ${productPrice}\n")
        delete=True
    elif productType in ["Té Snapple","Te Snapple","Mini Panque"]:
        if delete==False:
            pass
        else:
            clear(productAdd)
        productAdd=Label(mainWindow,text=f'¡Producto "{productType}" Agregado!',font=("Calibri",10),fg="green3")
        productAdd.pack()
        productPrice=18
        gain=gain+productPrice
        productTable.insert("",0,text=productType,values=(f"${productPrice}"))
        date=datetime.datetime.now()
        today=date.strftime("%d/%m/%Y %H:%M:%S")
        file=open("logs.txt","a")
        file.write(f"{today} - {user} ha facturado un {productType} a ${productPrice}\n")
        delete=True
    elif productType in ["Panini Jamon","Panini Jamón","Panini Jamón Pavo","Panini Jamon Pavo","Café 1/4","Cafe 1/4"]:
        if delete==False:
            pass
        else:
            clear(productAdd)
        productAdd=Label(mainWindow,text=f'¡Producto "{productType}" Agregado!',font=("Calibri",10),fg="green3")
        productAdd.pack()
        productPrice=65
        gain=gain+productPrice
        productTable.insert("",0,text=productType,values=(f"${productPrice}"))
        date=datetime.datetime.now()
        today=date.strftime("%d/%m/%Y %H:%M:%S")
        file=open("logs.txt","a")
        file.write(f"{today} - {user} ha facturado un {productType} a ${productPrice}\n")
        delete=True
    elif productType in ["Panini Selva Negra"]:
        if delete==False:
            pass
        else:
            clear(productAdd)
        productAdd=Label(mainWindow,text=f'¡Producto "{productType}" Agregado!',font=("Calibri",10),fg="green3")
        productAdd.pack()
        productPrice=85
        gain=gain+productPrice
        productTable.insert("",0,text=productType,values=(f"${productPrice}"))
        date=datetime.datetime.now()
        today=date.strftime("%d/%m/%Y %H:%M:%S")
        file=open("logs.txt","a")
        file.write(f"{today} - {user} ha facturado un {productType} a ${productPrice}\n")
        delete=True
    elif productType in ["Te Frio","Té Frio","Té","Te","Capuchino M","Moka M","Flat White M","Latte M","Chai M","Chocolate M"]:
        if delete==False:
            pass
        else:
            clear(productAdd)
        productAdd=Label(mainWindow,text=f'¡Producto "{productType}" Agregado!',font=("Calibri",10),fg="green3")
        productAdd.pack()
        productPrice=30
        gain=gain+productPrice
        productTable.insert("",0,text=productType,values=(f"${productPrice}"))
        date=datetime.datetime.now()
        today=date.strftime("%d/%m/%Y %H:%M:%S")
        file=open("logs.txt","a")
        file.write(f"{today} - {user} ha facturado un {productType} a ${productPrice}\n")
        delete=True
    elif productType in ["Adiccion","Chocoqueso","Pastel Zanahoria","Muss Guayaba","Muss Frutos",
    "Muss limon","Strudell","Corazon De Leon","Corazón De León","Gansito Ketto","Pinguino Ketto","Chescake Brownie",
    "Chescake Fresa","Beso De Chocolate","Crunch De Menta","Domo Mazapan","Domo Mazapán","Trufa","Tarta De Frutas"]:
        if delete==False:
            pass
        else:
            clear(productAdd)
        productAdd=Label(mainWindow,text=f'¡Producto "{productType}" Agregado!',font=("Calibri",10),fg="green3")
        productAdd.pack()
        productPrice=60
        gain=gain+productPrice
        productTable.insert("",0,text=productType,values=(f"${productPrice}"))
        date=datetime.datetime.now()
        today=date.strftime("%d/%m/%Y %H:%M:%S")
        file=open("logs.txt","a")
        file.write(f"{today} - {user} ha facturado un {productType} a ${productPrice}\n")
        delete=True
    elif productType in ["Golden Milk G","Frape Especial"]:
        if delete==False:
            pass
        else:
            clear(productAdd)
        productAdd=Label(mainWindow,text=f'¡Producto "{productType}" Agregado!',font=("Calibri",10),fg="green3")
        productAdd.pack()
        productPrice=45
        gain=gain+productPrice
        productTable.insert("",0,text=productType,values=(f"${productPrice}"))
        date=datetime.datetime.now()
        today=date.strftime("%d/%m/%Y %H:%M:%S")
        file=open("logs.txt","a")
        file.write(f"{today} - {user} ha facturado un {productType} a ${productPrice}\n")
        delete=True
    elif productType in ["Café 1kg","Cafe 1kg"]:
        if delete==False:
            pass
        else:
            clear(productAdd)
        productAdd=Label(mainWindow,text=f'¡Producto "{productType}" Agregado!',font=("Calibri",10),fg="green3")
        productAdd.pack()
        productPrice=265
        gain=gain+productPrice
        productTable.insert("",0,text=productType,values=(f"${productPrice}"))
        date=datetime.datetime.now()
        today=date.strftime("%d/%m/%Y %H:%M:%S")
        file=open("logs.txt","a")
        file.write(f"{today} - {user} ha facturado un {productType} a ${productPrice}\n")
        delete=True
    elif productType in [""]:
        if delete==False:
            pass
        else:
            clear(productAdd)
        productAdd=Label(mainWindow,text=f'¡Ingrese algún producto!',font=("Calibri",10),fg="red2")
        productAdd.pack()
        delete=True
    else:
        if delete==False:
            pass
        else:
            clear(productAdd)
        productAdd=Label(mainWindow,text=f'¡Producto "{productType}" NO EXISTE!',font=("Calibri",10),fg="red2")
        productAdd.pack()
        delete=True

# This function it's for the checkout window, tells the purchase value and confirms or declines it
# Esta funcion es para confirmar y rechazar la compra
def checkout():
    global gain, mainWindow,checkout,delete,productAdd
    if gain<=0:
        if delete==False:
            pass
        else:
            clear(productAdd)
        productAdd=Label(mainWindow,text=f'¡NO HAY PRODUCTOS REGISTRADOS!',font=("Calibri",10),fg="red2")
        productAdd.pack()
        delete=True
    else:
        checkout=Tk()
        checkout.resizable(0,0)
        checkout.iconbitmap("titleIcon.ico")
        checkout.geometry("295x215")
        checkout.title("Café DiFiore - Recibo")

        finalLabel=Label(checkout,text="Registro de Ingresos",font=("Helvetica",20,"bold"))
        finalLabel.pack(pady=2)
        finalLabel2=Label(checkout,text="Total a Pagar :",font=("Calibri",15))
        finalLabel2.pack(pady=2)
        checkoutLabel=Label(checkout,text=f"${gain}",font=("Calibri",20,"bold"),fg="green3")
        checkoutLabel.pack(pady=8)
        endButton=Button(checkout,text="Registrar",command=final)
        endButton.pack(pady=2)
        endButton2=Button(checkout,text="Cancelar",command=restart)
        endButton2.pack(pady=2)

# This Function it's my main window, not the root one, that's called "window"    
# Esta función es para la ventana pricipal donde se registran los productos.
def mainWindow():
    global mainWindow,imageLogo,IDTextBox,delete,productTable
    delete=False
    window.destroy()
    mainWindow=Tk()
    mainWindow.resizable(0,0)
    mainWindow.iconbitmap("titleIcon.ico")
    mainWindow.geometry("430x520")
    mainWindow.title("Café DiFiore - Administrador")

    imageLogo=PhotoImage(file="logoImage.gif")
    topLabel=Label(image=imageLogo)
    topLabel.pack()
    productTable=ttk.Treeview(mainWindow,columns=("#1",))
    productTable.heading("#0",text="     Nombre",anchor=W)
    productTable.heading("#1",text="Precio",anchor=W)
    productTable.pack()

    titleLabel=Label(mainWindow, text="Ingrese el Tipo de Producto :", font=("Calibri",15))
    titleLabel.pack()
    IDTextBox=Entry(mainWindow,font=("Calibri",12))
    IDTextBox.pack(pady=2)
    checkButton=Button(mainWindow,text="Aceptar",font=("Calibri",10),command=register)
    checkButton.pack(pady=4)
    checkOutButton=Button(mainWindow,text="Finalizar",font=("Calibri",10),command=checkout)
    checkOutButton.pack(pady=4)

# This function write on a txt file when a purchase is successful
# Cuando una compra es confirmada, esta función lo registra en un archivo de texto
def final():
    global checkout, gain
    file=open("ganancias.txt","a")
    file.write(f"{today} - {user} ha realizado una venta de ${gain}!\n")
    gain=0
    for i in productTable.get_children():
        productTable.delete(i)
    if delete==False:
        pass
    else:
        clear(productAdd)
    checkout.destroy()

# This function write on a txt file when a purchase is not successful
# Cuando una compra es rechazada o invalidada, esta función lo registra en un archivo de texto
def restart():
    global checkout,gain
    file=open("ganancias.txt","a")
    file.write(f"{today} - {user} ha cancelado una venta de ${gain}!\n")
    gain=0
    for i in productTable.get_children():
        productTable.delete(i)
    if delete==False:
        pass
    else:
        clear(productAdd)
    checkout.destroy()

# Root Window - Before Login Function
# Ventana Raiz - Esto viene antes de la función de logeo.
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
