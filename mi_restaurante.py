from tkinter import *
from tkinter import messagebox, filedialog
import random
import datetime
import sys
import os


# Variables globales
operador = ''
precios_comidas = [10.0, 15.0, 12.0, 8.0, 7.0, 5.0]
precios_bebidas = [2.0, 3.0, 5.0, 7.0, 4.0, 1.5]
precios_postres = [4.0, 6.0, 3.0, 2.5, 4.5, 5.5]

# IVA
IVA = 0.12


# ----------------------------------------------------------------
# Funciones
# Función para manejar los clics en los botones de la calculadora
def click_boton(valor):
    global operador
    operador = operador + str(valor)
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


# Función para limpiar el visor de la calculadora
def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)


# Función para calcular el resultado de la operación en la calculadora
def resultado():
    global operador
    res = str(round(eval(operador), 2))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, res)
    operador = ''


# Función para revisar los checkbuttons y habilitar/deshabilitar los campos de entrada
def revisar_check():
    # Comidas
    x = 0
    for c in cuadros_comidas:
        if variables_comidas[x].get() == 1:
            cuadros_comidas[x].config(state='normal')
            if cuadros_comidas[x].get() == '0':
                cuadros_comidas[x].delete(0, END)
            cuadros_comidas[x].focus()
        else:
            cuadros_comidas[x].config(state='disabled')
            texto_comidas[x].set('0')
        x += 1

    # Bebidas
    x = 0
    for b in cuadros_bebidas:
        if variables_bebidas[x].get() == 1:
            cuadros_bebidas[x].config(state='normal')
            if cuadros_bebidas[x].get() == '0':
                cuadros_bebidas[x].delete(0, END)
            cuadros_bebidas[x].focus()
        else:
            cuadros_bebidas[x].config(state='disabled')
            texto_bebidas[x].set('0')
        x += 1

    # Postres
    x = 0
    for p in cuadros_postres:
        if variables_postres[x].get() == 1:
            cuadros_postres[x].config(state='normal')
            if cuadros_postres[x].get() == '0':
                cuadros_postres[x].delete(0, END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state='disabled')
            texto_postres[x].set('0')
        x += 1


# Función para calcular el total
def total():
    # Calcular el costo de la comida
    sub_total_comida = 0
    p = 0
    for cant in texto_comidas:
        sub_total_comida = sub_total_comida + (float(cant.get()) * precios_comidas[p])
        p += 1

    # Calcular el costo de la bebida
    sub_total_bebida = 0
    p = 0
    for cant in texto_bebidas:
        sub_total_bebida = sub_total_bebida + (float(cant.get()) * precios_bebidas[p])
        p += 1

    # Calcular el costo del postre
    sub_total_postre = 0
    p = 0
    for cant in texto_postres:
        sub_total_postre = sub_total_postre + (float(cant.get()) * precios_postres[p])
        p += 1

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postre
    impuesto = sub_total * IVA
    total_final = sub_total + impuesto

    # Actualizar los campos de entrada
    texto_costo_comida.set(f"${round(sub_total_comida, 2)}")
    texto_costo_bebida.set(f"${round(sub_total_bebida, 2)}")
    texto_costo_postre.set(f"${round(sub_total_postre, 2)}")
    texto_subtotal.set(f"${round(sub_total, 2)}")
    texto_impuesto.set(f"${round(impuesto, 2)}")
    texto_total.set(f"${round(total_final, 2)}")


# Función para generar el recibo
def generar_recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f"N# - {random.randint(1000, 9999)}"
    fecha = datetime.datetime.now()
    fecha_recibo = f"{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}:{fecha.second}"
    texto_recibo.insert(END, f"Recibo:\t{num_recibo}\t\t{fecha_recibo}\n")
    texto_recibo.insert(END, f"*"*67 + "\n")
    texto_recibo.insert(END, "Items\t\tCant.\tCosto Items\n")
    texto_recibo.insert(END, f"-"*80 + "\n")

    # Comidas
    x = 0
    for comidas in texto_comidas:
        if int(comidas.get()) != 0:
            texto_recibo.insert(END, f"{lista_comidas[x]}\t\t{comidas.get()}\t${float(comidas.get()) * precios_comidas[x]}\n")
        x += 1

    # Bebidas
    x = 0
    for bebidas in texto_bebidas:
        if int(bebidas.get()) != 0:
            texto_recibo.insert(END, f"{lista_bebidas[x]}\t\t{bebidas.get()}\t${float(bebidas.get()) * precios_bebidas[x]}\n")
        x += 1

    # Postres
    x = 0
    for postres in texto_postres:
        if int(postres.get()) != 0:
            texto_recibo.insert(END, f"{lista_postres[x]}\t\t{postres.get()}\t${float(postres.get()) * precios_postres[x]}\n")
        x += 1

    texto_recibo.insert(END, f"-" * 80 + "\n")
    texto_recibo.insert(END, f"Costo de la Comida:\t\t\t{texto_costo_comida.get()}\n")
    texto_recibo.insert(END, f"Costo de la Bebida:\t\t\t{texto_costo_bebida.get()}\n")
    texto_recibo.insert(END, f"Costo del Postre:\t\t\t{texto_costo_postre.get()}\n")
    texto_recibo.insert(END, f"-" * 80 + "\n")
    texto_recibo.insert(END, f"Subtotal:\t\t\t{texto_subtotal.get()}\n")
    texto_recibo.insert(END, f"Impuesto:\t\t\t{texto_impuesto.get()}\n")
    texto_recibo.insert(END, f"Total:\t\t\t{texto_total.get()}\n")
    texto_recibo.insert(END, f"*"*67 + "\n")
    texto_recibo.insert(END, "Gracias por su compra\n")
    texto_recibo.insert(END, "¡Vuelva pronto!\n")


# Función para guardar el recibo en un archivo de texto
def guardar_recibo():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo("Información", "Su recibo ha sido guardado")


# Función para reiniciar el sistema
def reiniciar():
    texto_recibo.delete(0.1, END)
    # Reiniciar todas las variables
    for texto in texto_comidas:
        texto.set('0')
    for texto in texto_bebidas:
        texto.set('0')
    for texto in texto_postres:
        texto.set('0')
    # Reiniciar los cuadros de comidas
    for cuadro in cuadros_comidas:
        cuadro.config(state='disabled')
    for cuadro in cuadros_bebidas:
        cuadro.config(state='disabled')
    for cuadro in cuadros_postres:
        cuadro.config(state='disabled')
    # Reiniciar los checkbuttons
    for var in variables_comidas:
        var.set(0)
    for var in variables_bebidas:
        var.set(0)
    for var in variables_postres:
        var.set(0)
    # Reiniciar los costos
    texto_costo_comida.set('')
    texto_costo_bebida.set('')
    texto_costo_postre.set('')
    texto_subtotal.set('')
    texto_impuesto.set('')
    texto_total.set('')


# ----------------------------------------------------------------
# Inicializar la ventana principal
root = Tk()


# Tamaño de la ventana
root.geometry("1020x630+200+100")


# Evitar que la ventana se pueda redimensionar
root.resizable(None, None)


# Título de la ventana
root.title("Mi Restaurante - Sistema de Facturación")


# Color de fondo de la ventana
root.config(bg="#06161a")


# Icono de la ventana
if getattr(sys, 'frozen', False):
    ruta_icono = os.path.join(sys._MEIPASS, 'icons', 'icon.ico')
else:
    ruta_icono = './icons/icon.ico'

root.iconbitmap(ruta_icono)


# ----------------------------------------------------------------
# Panel Superior
panel_superior = Frame(root, bd=1, relief='flat')
panel_superior.pack(side='top')


# Etiqueta del título
etiqueta_titulo = Label(panel_superior, text="Sistema de Facturación", fg="#cdd5db", bg="#072e33", font=("Dosis", 30, 'bold'), width=40)
etiqueta_titulo.grid(row=0, column=0)


# ----------------------------------------------------------------
# Panel Izquierdo
panel_izquierdo = Frame(root, bd=1, relief='flat')
panel_izquierdo.pack(side='left')


# Panel Costos
panel_costos = Frame(panel_izquierdo, bd=1, relief='flat', bg="#0c7075")
panel_costos.pack(side='bottom')


# Panel Comidas
panel_comidas = LabelFrame(panel_izquierdo, text="Comida", font=("Dosis", 19, 'bold'), bd=1, relief='flat', fg="#cdd5db", bg="#072e33")
panel_comidas.pack(side='left')


# Panel Bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text="Bebidas", font=("Dosis", 19, 'bold'), bd=1, relief='flat', fg="#cdd5db", bg="#072e33")
panel_bebidas.pack(side='left')


# Panel Postres
panel_postres = LabelFrame(panel_izquierdo, text="Postres", font=("Dosis", 19, 'bold'), bd=1, relief='flat', fg="#cdd5db", bg="#072e33")
panel_postres.pack(side='left')


# ----------------------------------------------------------------
# Panel Derecho
panel_derecho = Frame(root, bd=1, relief='flat')
panel_derecho.pack(side='right')


# Panel Calculadora
panel_calculadora = Frame(panel_derecho, bd=1, relief='flat')
panel_calculadora.pack()


# Panel Recibo
panel_recibo = Frame(panel_derecho, bd=1, relief='flat')
panel_recibo.pack()


# Panel Botones
panel_botones = Frame(panel_derecho, bd=1, relief='flat')
panel_botones.pack()


# ----------------------------------------------------------------
# Lista de productos
lista_comidas = ['Pollo', 'Carne', 'Pescado', 'Arroz', 'Ensalada', 'Sopa']
lista_bebidas = ['Agua', 'Refresco', 'Cerveza', 'Vino', 'Jugo', 'Café']
lista_postres = ['Helado', 'Pastel', 'Fruta', 'Galleta', 'Flan', 'Tarta']


# Loops para crear etiquetas y campos de entrada
# Comidas
variables_comidas = []
cuadros_comidas = []
texto_comidas = []
contador = 0
for comida in lista_comidas:
    # Crear las listas
    variables_comidas.append('')
    variables_comidas[contador] = IntVar()
    comida = Checkbutton(panel_comidas, text=comida, font=("Dosis", 16, 'bold'), bg="#072e33", fg="#cdd5db",  onvalue=1, offvalue=0 , variable=variables_comidas[contador], command=revisar_check)
    comida.grid(row=contador, column=0, sticky='w')

    # Crear el campo de entrada
    cuadros_comidas.append('')
    texto_comidas.append('')
    texto_comidas[contador] = StringVar()
    texto_comidas[contador].set('0')
    cuadros_comidas[contador] = Entry(panel_comidas, font=("Dosis", 16, 'bold'), bd=1, width=6, state='disabled', textvariable=texto_comidas[contador])
    cuadros_comidas[contador].grid(row=contador, column=1)
    contador += 1

# Bebidas
variables_bebidas = []
cuadros_bebidas = []
texto_bebidas = []
contador = 0
for bebida in lista_bebidas:
    # Crear las listas
    variables_bebidas.append('')
    variables_bebidas[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, text=bebida, font=("Dosis", 16, 'bold'), bg="#072e33", fg="#cdd5db", onvalue=1, offvalue=0 , variable=variables_bebidas[contador], command=revisar_check)
    bebida.grid(row=contador, column=0, sticky='w')

    # Crear el campo de entrada
    cuadros_bebidas.append('')
    texto_bebidas.append('')
    texto_bebidas[contador] = StringVar()
    texto_bebidas[contador].set('0')
    cuadros_bebidas[contador] = Entry(panel_bebidas, font=("Dosis", 16, 'bold'), bd=1, width=6, state='disabled', textvariable=texto_bebidas[contador])
    cuadros_bebidas[contador].grid(row=contador, column=1)
    contador += 1

# Postres
variables_postres = []
cuadros_postres = []
texto_postres = []
contador = 0
for postre in lista_postres:
    # Crear las listas
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postre = Checkbutton(panel_postres, text=postre, font=("Dosis", 16, 'bold'), bg="#072e33", fg="#cdd5db", onvalue=1, offvalue=0 , variable=variables_postres[contador], command=revisar_check)
    postre.grid(row=contador, column=0, sticky='w')

    # Crear el campo de entrada
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres, font=("Dosis", 16, 'bold'), bd=1, width=6, state='disabled', textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=contador, column=1)
    contador += 1


# ----------------------------------------------------------------
# Etiquetas y campos de entrada para costos

# Costo Comida
etiqueta_costo_comida = Label(panel_costos, text="Costo Comida", font=("Dosis", 14, 'bold'), bg="#0c7075", fg="#cdd5db")
etiqueta_costo_comida.grid(row=0, column=0, sticky='w')
# Campo de entrada
texto_costo_comida = StringVar() # Variable para el campo de entrada
cuadro_costo_comida = Entry(panel_costos, font=("Dosis", 16, 'bold'), bd=1, width=10, state='readonly', textvariable=texto_costo_comida)
cuadro_costo_comida.grid(row=0, column=1, padx=27)


# Costo Bebida
etiqueta_costo_bebida = Label(panel_costos, text="Costo Bebida", font=("Dosis", 14, 'bold'), bg="#0c7075", fg="#cdd5db")
etiqueta_costo_bebida.grid(row=1, column=0, sticky='w')
# Campo de entrada
texto_costo_bebida = StringVar() # Variable para el campo de entrada
cuadro_costo_bebida = Entry(panel_costos, font=("Dosis", 16, 'bold'), bd=1, width=10, state='readonly', textvariable=texto_costo_bebida)
cuadro_costo_bebida.grid(row=1, column=1, padx=27)


# Costo Postre
etiqueta_costo_postre = Label(panel_costos, text="Costo Postre", font=("Dosis", 14, 'bold'), bg="#0c7075", fg="#cdd5db")
etiqueta_costo_postre.grid(row=2, column=0, sticky='w')
# Campo de entrada
texto_costo_postre = StringVar() # Variable para el campo de entrada
cuadro_costo_postre = Entry(panel_costos, font=("Dosis", 16, 'bold'), bd=1, width=10, state='readonly', textvariable=texto_costo_postre)
cuadro_costo_postre.grid(row=2, column=1, padx=27)


# Subtotal
etiqueta_subtotal = Label(panel_costos, text="Subtotal", font=("Dosis", 14, 'bold'), bg="#0c7075", fg="#cdd5db")
etiqueta_subtotal.grid(row=0, column=2, sticky='w')
# Campo de entrada
texto_subtotal = StringVar() # Variable para el campo de entrada
cuadro_subtotal = Entry(panel_costos, font=("Dosis", 16, 'bold'), bd=1, width=10, state='readonly', textvariable=texto_subtotal)
cuadro_subtotal.grid(row=0, column=3, padx=27)


# Impuesto
etiqueta_impuesto = Label(panel_costos, text="Impuesto", font=("Dosis", 14, 'bold'), bg="#0c7075", fg="#cdd5db")
etiqueta_impuesto.grid(row=1, column=2, sticky='w')
# Campo de entrada
texto_impuesto = StringVar() # Variable para el campo de entrada
cuadro_impuesto = Entry(panel_costos, font=("Dosis", 16, 'bold'), bd=1, width=10, state='readonly', textvariable=texto_impuesto)
cuadro_impuesto.grid(row=1, column=3, padx=27)


# Total
etiqueta_total = Label(panel_costos, text="Total", font=("Dosis", 14, 'bold'), bg="#0c7075", fg="#cdd5db")
etiqueta_total.grid(row=2, column=2, sticky='w')
# Campo de entrada
texto_total = StringVar() # Variable para el campo de entrada
cuadro_total = Entry(panel_costos, font=("Dosis", 16, 'bold'), bd=1, width=10, state='readonly', textvariable=texto_total)
cuadro_total.grid(row=2, column=3, padx=27)


# ----------------------------------------------------------------
# Botones
botones = ['Total', 'Recibo', 'Guardar', 'Resetear']
botones_creados = []
columnas = 0
for boton in botones:
    boton = Button(panel_botones, text=boton, font=("Dosis", 14, 'bold'), fg="#cdd5db", bg="#072e33", bd=1, width=8)
    botones_creados.append(boton)
    boton.grid(row=0, column=columnas)
    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=generar_recibo)
botones_creados[2].config(command=guardar_recibo)
botones_creados[3].config(command=reiniciar)


# ----------------------------------------------------------------
# Área de texto para el recibo
texto_recibo = Text(panel_recibo, font=("Dosis", 12, 'bold'), bd=1, width=45, height=10)
texto_recibo.grid(row=0, column=0)


# ----------------------------------------------------------------
# Calculadora
# Visor de la calculadora
visor_calculadora = Entry(panel_calculadora, font=("Dosis", 16, 'bold'), bd=1, width=34)
visor_calculadora.grid(row=0, column=0, columnspan=4)

# Botones de la calculadora
botones_calculadora = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', 'x',
    'C', '0', '=', '/'
]
botones_guardados = []
fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora, text=boton, font=("Dosis", 14, 'bold'), fg="#cdd5db", bg="#072e33", bd=1, width=8)
    botones_guardados.append(boton)
    boton.grid(row=fila, column=columna)
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1


# Asignar funciones a los botones de la calculadora
botones_guardados[0].config(command=lambda: click_boton('7'))
botones_guardados[1].config(command=lambda: click_boton('8'))
botones_guardados[2].config(command=lambda: click_boton('9'))
botones_guardados[3].config(command=lambda: click_boton('+'))
botones_guardados[4].config(command=lambda: click_boton('4'))
botones_guardados[5].config(command=lambda: click_boton('5'))
botones_guardados[6].config(command=lambda: click_boton('6'))
botones_guardados[7].config(command=lambda: click_boton('-'))
botones_guardados[8].config(command=lambda: click_boton('1'))
botones_guardados[9].config(command=lambda: click_boton('2'))
botones_guardados[10].config(command=lambda: click_boton('3'))
botones_guardados[11].config(command=lambda: click_boton('*'))
botones_guardados[12].config(command=borrar)
botones_guardados[13].config(command=lambda: click_boton('0'))
botones_guardados[14].config(command=resultado)
botones_guardados[15].config(command=lambda: click_boton('/'))


# Evitar que la ventana se cierre
root.mainloop()