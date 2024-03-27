
import tkinter as tk
from tkinter import ttk, messagebox, END, Scrollbar, Text, Label, filedialog

import pyperclip

import matplotlib.pyplot as plt

import csv
import openpyxl
import xlwt
import os

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


from tkinter import *


from Clientes import CClientes
from Conexion import *

import re

class FormularioClientes:
    
    global TextBoxId
    TextBoxId = None
    global TextBoxNombre
    TextBoxNombre = None
    global TextBoxTelefono
    TextBoxTelefono = None
    global comboP
    comboP = None
    global comboF
    comboF = None
    global TextBoxFalla
    TextBoxFalla = None
    global TextBoxSolucion
    TextBoxSolucion = None
    global comboN
    comboN = None
    global groupBox
    groupBox = None
    global groupBoxB
    groupBoxB = None
    global groupBoxR
    groupBoxR = None
    global groupBoxE
    groupBoxE = None
    global groupBoxT
    groupBoxT = None
    global tree
    tree = None
    global base
    base = None
    global comboBuscarPor
    comboBuscarPor = None
    global TextBoxValorBusqueda
    TextBoxValorBusqueda = None
    
def __init__():
    pass

            
def on_scroll(*args):
    TextBoxFalla.yview(*args)
    TextBoxSolucion.yview(*args)  

def validar_telefono(entrada):
    # Patrón regex que acepta solo números y caracteres especiales
    patron = r'^[0-9\-+]+$'
    return re.match(patron, entrada) is not None

def limitar_caracteres(event):
    # Limitar la longitud del campo de entrada a 15 caracteres
    if len(TextBoxTelefono.get()) >= 15:
        return False
    return True

def Formulario():
        
    global TextBoxId
    global TextBoxNombre
    global TextBoxTelefono
    global comboP
    global comboF
    global TextBoxFalla
    global TextBoxSolucion
    global comboN
    global groupBox
    global groupBoxB
    global groupBoxR
    global groupBoxE
    global groupBoxT
    global tree
    global base
    global LabelNombre
    global comboBuscarPor
    global TextBoxValorBusqueda
    try:
        base = Tk()
        base.geometry("1700x700")
        base.title("Formlario Clientes")
        base.iconbitmap("images/pe.ico")
        
        # Cambiar el color de fondo de la ventana principal
        base.configure(bg='#C5E0DC')
        
        groupBox = LabelFrame(base, text="DATOS DEL CLIENTE", padx=15,pady=1,font=('arial',10,'bold'), bg='#9DBEBB', labelanchor='n')
        groupBox.grid(row=0,column=0,padx=10,pady=10)
        
            
            #datos: Nombre, Telefono, Financiamiento, Falla del cliente, Soporte brindado, Tier 1, Fecha
        
        LabelId=Label(groupBox,text="ID: ",width=13,font=("arial",10,"bold"),bg='#9DBEBB')
        LabelId.grid(row=0,column=0)
        TextBoxId= Entry(groupBox, width=40,font=("arial",11))
        TextBoxId.grid(row=0,column=1, sticky="w")
        
        
            
        LabelNombre=Label(groupBox,text="NOMBRE:",width=13,font=("arial",10,"bold"),bg='#9DBEBB')
        LabelNombre.grid(row=1,column=0)
        TextBoxNombre= Entry(groupBox, width=40, font=("arial",11))
        TextBoxNombre.grid(row=1,column=1, sticky="w")
            
        LabelTelefono=Label(groupBox,text="TELEFONO:",width=13,font=("arial",10,"bold"),bg='#9DBEBB')
        LabelTelefono.grid(row=2,column=0)
        validacion = base.register(validar_telefono)
        TextBoxTelefono= Entry(groupBox, width=40, font=("arial",11),validate="key", validatecommand=(validacion, '%S'))
        TextBoxTelefono.grid(row=2,column=1, sticky="w")
        TextBoxTelefono.bind('<Key>', limitar_caracteres)
        
        LabelPueblo=Label(groupBox,text="PUEBLO:",width=13,font=("arial",10,"bold"),bg='#9DBEBB')
        LabelPueblo.grid(row=3,column=0)
        seleccion=tk.StringVar()
        comboP=ttk.Combobox(groupBox,values=["Adjuntas","Aguada","Aguadilla","Aguas Buenas","Aibonito","Añasco",
                                             "Arecibo","Arroyo","Barceloneta","Barranquitas","Bayamón","Cabo Rojo",
                                             "Caguas","Camuy","Canóvanas","Carolina","Cataño","Cayey",
                                             "Ceiba","Ciales","Cidra","Coamo","Comerío","Corozal",
                                             "Culebra","Dorado","Fajardo","Florida","Guánica","Guayama",
                                             "Guayanilla","Guaynabo","Gurabo","Hatillo","Hormigueros","Humacao",
                                             "Isabel II","Isabela","Jayuya","Juana Díaz","Juncos","La Parguera",
                                             "Lajas Pueblo","Lares","Las Marías","Las Piedras","Loíza","Luquillo",
                                             "Manatí","Maricao","Maunabo","Mayagüez","Moca","Morovis",
                                             "Naguabo","Naranjito","Orocovis","Patillas","Peñuelas","Ponce",
                                             "Quebradillas","Rincón","Río Grande","Sabana Grande","Salinas","San Germán",
                                             "San Lorenzo","San Juan","San Sebastián","Santa Isabel","Toa Alta","Toa Baja","Trujillo Alto",
                                             "Utuado","Vega Alta","Vega Baja","Villalba","Yabucoa","Yauco"],textvariable=seleccion, state="readonly",width=43, font=("arial",9))
        comboP.grid(row=3,column=1, sticky="w")
        seleccion.set("")
           
        LabelFinanciamiento=Label(groupBox,text="FINANCIAMIENTO:",width=13,font=("arial",10,"bold"),bg='#9DBEBB',padx=10)
        LabelFinanciamiento.grid(row=4,column=0)
        seleccion=tk.StringVar()
        comboF=ttk.Combobox(groupBox,values=["Cash","Sunnova","CDBG"],textvariable=seleccion, state="readonly",width=43, font=("arial",9))
        comboF.grid(row=4,column=1, sticky="w")
        seleccion.set("Cash")
            
        LabelFalla=Label(groupBox,text="FALLA \nDEL CLIENTE:",width=13,font=("arial",10,"bold"),bg='#9DBEBB')
        LabelFalla.grid(row=5,column=0)
        TextBoxFalla= Text(groupBox, width=40, height=5, font=("arial",11))
        TextBoxFalla.grid(row=5,column=1)
        
        scrollbar = Scrollbar(groupBox, command=on_scroll)
        scrollbar.grid(row=5, column=2, sticky='ns')
        TextBoxFalla.config(yscrollcommand=scrollbar.set)
            
        LabelSolucion=Label(groupBox,text="SOPORTE \nBRINDADO:",width=13,font=("arial",10,"bold"),bg='#9DBEBB')
        LabelSolucion.grid(row=6,column=0)
        TextBoxSolucion= Text(groupBox, width=40, height=5, font=("arial",11))
        TextBoxSolucion.grid(row=6,column=1)
        
        scrollbar = Scrollbar(groupBox, command=on_scroll)
        scrollbar.grid(row=6, column=2, sticky='ns')
        TextBoxSolucion.config(yscrollcommand=scrollbar.set)
            
        LabelTier=Label(groupBox,text="TIER 1:",width=13,font=("arial",10, "bold"),bg='#9DBEBB')
        LabelTier.grid(row=7,column=0)
        seleccionN=tk.StringVar()
        comboN=ttk.Combobox(groupBox,values=["Braian Camilo Diaz Linares","Juan Carlos Vallejo","Sebastian Riaño","Jose Miguel Morales"],textvariable=seleccionN, state="readonly",width=43, font=("arial",9))
        comboN.grid(row=7,column=1, sticky="w")
        
        
        groupBoxB = LabelFrame(base, text="BUSCAR REGISTRO", padx=82,pady=1,font=('arial',10,'bold'), bg='#92BEBB', labelanchor='n')
        groupBoxB.grid(row=1,column=0,padx=10,pady=(0,120))
         
         
        LabelBuscarPor=Label(groupBoxB, text="Buscar por:",width=13,font=("arial",11,"bold"),bg='#9DBEBB')
        LabelBuscarPor.grid(row=0, column=0,padx=(0, 40))
        
        comboBuscarPor = ttk.Combobox(groupBoxB, values=["Nombre", "Telefono"], state="readonly", width=30, font=("arial", 9))
        comboBuscarPor.grid(row=0, column=1, sticky="w")
        
        LabelValorBusqueda = Label(groupBoxB, text="Valor:", width=7, font=("arial", 11, "bold"), bg='#9DBEBB')
        LabelValorBusqueda.grid(row=1, column=0,padx=(0, 40))

        TextBoxValorBusqueda = Text(groupBoxB,width=29, height=0, font=("arial",11))
        TextBoxValorBusqueda.grid(row=1, column=1)

                  
        btn_guardar = Button(groupBox, text='Guardar', command=guardarRegistros,bg='#F4E9CD',font=("arial",12))
        btn_modificar = Button(groupBox, text='Modificar',command=ModificarRegistros,bg='#F4E9CD',font=("arial",12))
        btn_limpiar = Button(groupBox, text='Limpiar', command=limpiar_campos,bg='#F4E9CD',font=("arial",12),padx=9)
        btn_copiar = Button(groupBox, text='Copiar', command=copiar_campos,bg='#F4E9CD',font=("arial",12),padx=6)
        btn_borrar = Button(groupBox, text='Borrar', command=EliminarRegistros,bg='#F4E9CD',font=("arial",12),padx=11)
        btn_actualizar = Button(groupBox, text='Actualizar', command=ActualizarTabla,bg='#F4E9CD',font=("arial",12))
        btn_buscar = Button(groupBoxB, text='Buscar', command=buscar_cliente, bg='#F4E9CD', font=("arial", 12),padx=9)
        btn_generar_reporte = Button(groupBoxB, text='Generar Reporte CSV', command=guardar_reporte, bg='#F4E9CD', font=("arial",12))

        

        # Mostrar los botones en la ventana
        btn_guardar.grid(row=9, column=0,pady=(15, 20))
        btn_modificar.grid(row=9, column=1,pady=(15, 20))
        btn_limpiar.grid(row=9, column=2,pady=(15, 20))
        btn_copiar.grid(row=11, column=0,pady=(5, 10))
        btn_borrar.grid(row=11, column=1,pady=(5, 10))
        btn_actualizar.grid(row=11, column=2,pady=(5, 10))
        
        btn_buscar.grid(row=2, column=1, pady=(5, 10), padx=(0, 119))
        btn_generar_reporte.grid(row=3, column=1, pady=(5, 10))
         
        
         
        groupBoxR = LabelFrame(base, text="LISTA DE REGISTRO",font=('arial',10,'bold'), padx=0, pady=0, labelanchor='n')
        groupBoxR.grid(row=0,column=1,padx=0,pady=10)
        
        tree = ttk.Treeview(groupBoxR,columns=("ID","NOMBRE","TELEFONO","PUEBLO","FINANCIAMIENTO","FALLA DEL CLIENTE","SOPORTE BIRNDADO","TIER 1"),show='headings',height=20,)
        tree.grid(row=0, column=0, sticky="nsew")
        
        column_widths = [30, 200, 80, 80, 110, 200, 200, 150]  # Anchos de las columnas
        columns = ["ID","NOMBRE","TELEFONO","PUEBLO","FINANCIAMIENTO","FALLA DEL CLIENTE","SOPORTE BIRNDADO","TIER 1"]
        for i, (column, width) in enumerate(zip(columns, column_widths), start=1):
            tree.column(f"#{i}", anchor=CENTER)
            tree.heading(f"#{i}", text=column)
            tree.column(f"#{i}", width=width)

        scrollbar_vertical = Scrollbar(groupBoxR, orient=VERTICAL, command=tree.yview)
        scrollbar_vertical.grid(row=0, column=1, sticky="ns")
        tree.configure(yscrollcommand=scrollbar_vertical.set)
        
        
        for row in CClientes.MostrarClientes():
            tree.insert("","end",values=row)
        
        #ejecutar la funcion al hacer clic y mostar el resultado en los Entry
        tree.bind("<<TreeviewSelect>>",seleccionarRegistro)
        tree.grid(row=0, column=0, sticky="nsew")



        groupBoxE = LabelFrame(base, text="REGISTRO POR FINANCIAMIENTO",font=('arial',10,'bold'), padx=0, pady=0, labelanchor='n')
        groupBoxE.grid(row=1,column=1,padx=(0,766),pady=(0,18))
        actualizarTreeView()
        
        groupBoxT = LabelFrame(base, text="REGISTRO INGRESADOS POR TIER",font=('arial',10,'bold'), padx=0, pady=0, labelanchor='n')
        groupBoxT.grid(row=1,column=1,padx=(315,0),pady=(0,18))
        grafica_Tier()
            
        
        
     
            
        base.mainloop()
    except ValueError as error:
        print("Error al mostrar la interfaz, error: {}".format(error))


def grafica_Tier():
    try:
        registros = CClientes.MostrarClientes()
        tier_count = {}
        for registro in registros:
            tier = registro[7]
            if tier in tier_count:
                tier_count[tier] += 1
            else:
                tier_count[tier] = 1

        # Preparar los datos para la gráfica de barras
        labels = list(tier_count.keys())
        sizes = list(tier_count.values())

        # Crear la gráfica de barras
        figura, ax = plt.subplots(figsize=(7.5, 2))
        ax.bar(labels, sizes, color='skyblue')
        ax.set_ylabel('Cantidad de Registros',fontsize=8)
        ax.grid(True)

        # Mostrar el valor de cada barra
        for i, v in enumerate(sizes):
            ax.text(i, v + 0.2, str(v), ha='center', va='bottom')
            
        ax.tick_params(axis='x', labelsize=7)
        # Mostrar la gráfica
        canvas_barras = FigureCanvasTkAgg(figura, master=groupBoxT)
        canvas_barras.draw()
        canvas_barras.get_tk_widget().grid(row=1, column=1, sticky="nsew")  
        
        
    except Exception as e:
        print("Error al mostrar la lista de registros y la gráfica de torta:", e)
       

def guardarRegistros():
        

        
    try:
        #verificar si los botones funcionan
        if not (TextBoxNombre.get() and TextBoxTelefono.get() and comboP.get() and comboF.get() and TextBoxFalla.get("1.0", "end-1c") and TextBoxSolucion.get("1.0", "end-1c") and comboN.get()):
            messagebox.showerror("Error", "Todos los campos deben ser llenados.")
            return
        Nombre = TextBoxNombre.get()
        Telefono = TextBoxTelefono.get()
        Pueblo = comboP.get()
        Financiamiento = comboF.get()
        Falla = TextBoxFalla.get("1.0", "end-1c")
        Solucion = TextBoxSolucion.get("1.0", "end-1c")
        Tier = comboN.get()
            
        cliente = CClientes()
        cliente.IngresarClientes(Nombre, Telefono, Pueblo, Financiamiento, Falla, Solucion, Tier)
        messagebox.showinfo("Informacion","Los datos fueron guardados")
        
        actualizarTreeView()
        grafica_Tier()
        #limpiar campos
        TextBoxNombre.delete(0, END)
        TextBoxTelefono.delete(0, END)
        comboP.set('')
        comboF.set('')  # Limpiar la selección de comboF
        TextBoxFalla.delete("1.0", "end-1c")
        TextBoxSolucion.delete("1.0", "end-1c")
        comboN.set('')
        
    except ValueError as error:
        print("Error al ingresar los datos {}".format(error))
        
        
def actualizarTreeView():
    global tree
    
    try:
        #borrar todos los elementos actuales del treeView
        tree.delete(*tree.get_children())
        
        #obtener los nuevos datos a mostrar
        datos = CClientes.MostrarClientes()
        
        #insertar los nuevos datos en el treeView
        for row in datos:
            tree.insert("","end",values=row)

        
        # Obtener los datos de financiamiento de los registros
        financiamiento_count = {}
        for registro in datos:
            financiamiento = registro[4]
            if financiamiento in financiamiento_count:
                financiamiento_count[financiamiento] += 1
            else:
                financiamiento_count[financiamiento] = 1

        # Preparar los datos para la gráfica de torta
        labels = list(financiamiento_count.keys())
        sizes = list(financiamiento_count.values())

        plt.clf()
        # Crear la gráfica de torta
        figura, ax = plt.subplots(figsize=(3, 2))
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        ax.set_title('Registros por financiamiento')

        # Crear el canvas para la gráfica de torta
        canvas = FigureCanvasTkAgg(figura, master=groupBoxE)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=1, sticky="nsew")

        # Agregar el treeview a la ventana principal  
    
    except ValueError as error:
        print("Error al actualizar la tabla {}".format(error))

def seleccionarRegistro(event):
    try:
        #obtener id del elemento selecionado
        itemSeleccionado= tree.focus()
        
        if itemSeleccionado:
            #obtener valores de la columna
            values=tree.item(itemSeleccionado)['values']
            
            #establecer valores en los botones
            TextBoxId.delete(0,END)
            TextBoxId.insert(0,values[0])
            TextBoxNombre.delete(0,END)
            TextBoxNombre.insert(0,values[1])
            TextBoxTelefono.delete(0,END)
            TextBoxTelefono.insert(0,values[2])
            comboP.set(values[3])
            comboF.set(values[4])
            TextBoxFalla.delete("1.0", "end-1c")
            TextBoxFalla.insert("1.0", "",0,values[5])
            TextBoxSolucion.delete("1.0", "end-1c")
            TextBoxSolucion.insert("1.0", "",0,values[6])
            comboN.set(values[7])
    except ValueError as error:
        print("Error al seleccionar registro {}".format(error))


def ModificarRegistros():
        
    global TextBoxId, TextBoxNombre, TextBoxTelefono, comboP, comboF, TextBoxFalla, TextBoxSolucion, comboN, groupBox
        
    try:
        #verificar si los botones funcionan
        if not TextBoxId.get():
            messagebox.showwarning("Advertencia", "Por favor, seleccione un registro para modificar.")
            return
        
        confirmacion = messagebox.askyesno("Confirmar modificación", "¿Está seguro de que desea modificar los datos seleccionados?")
        if confirmacion:
            Usuarioid = TextBoxId.get()
            Nombre = TextBoxNombre.get()
            Telefono = TextBoxTelefono.get()
            Pueblo = comboP.get()
            Financiamiento = comboF.get()
            Falla = TextBoxFalla.get("1.0", "end-1c")
            Solucion = TextBoxSolucion.get("1.0", "end-1c")
            Tier = comboN.get()
            
            cliente = CClientes()
            cliente.ModificarClientes(Usuarioid, Nombre, Telefono, Pueblo, Financiamiento, Falla, Solucion, Tier)
            messagebox.showinfo("Información", "Los datos fueron actualizados")
            
            actualizarTreeView()
            grafica_Tier()
            
            # Limpiar campos
            TextBoxId.delete(0, END)
            TextBoxNombre.delete(0, END)
            TextBoxTelefono.delete(0, END)
            comboP.set('')
            comboF.set('')  # Limpiar la selección de comboF
            TextBoxFalla.delete("1.0", "end-1c")
            TextBoxSolucion.delete("1.0", "end-1c")
            comboN.set('')
        
    except ValueError as error:
        print("Error al modificar los datos {}".format(error))
        

def EliminarRegistros():
        
    global TextBoxId
        
    try:
        #verificar si los botones funcionan
        if not TextBoxId.get():
            messagebox.showwarning("Advertencia", "Por favor, seleccione un registro para eliminar.")
            return
        
        confirmacion = messagebox.askyesno("Confirmar eliminación", "¿Está seguro de que desea eliminar los datos seleccionados?")
        if confirmacion:
            Usuarioid = TextBoxId.get()
            
            cliente = CClientes()
            cliente.EliminarClientes(Usuarioid)
            messagebox.showinfo("Información", "Los datos fueron eliminados")
            
            actualizarTreeView()
            grafica_Tier()
            
            #limpiar campos
        TextBoxId.delete(0, END)
        TextBoxNombre.delete(0, END)
        TextBoxTelefono.delete(0, END)
        comboP.set('')
        comboF.set('')  # Limpiar la selección de comboF
        TextBoxFalla.delete("1.0", "end-1c")
        TextBoxSolucion.delete("1.0", "end-1c")
        comboN.set('')
        
    except ValueError as error:
        print("Error al modificar los datos {}".format(error))
        

def copiar_campos():
    
    labels = ["NOMBRE:  ","TELEFONO:  ","PUEBLO:  ","FINANCIAMIENTO:  ","FALLA DEL CLIENTE:  ","SOPORTE BIRNDADO:  ","TIER 1:  "]
    valores = [TextBoxNombre.get(), TextBoxTelefono.get(), comboP.get(), comboF.get(), TextBoxFalla.get("1.0", "end-1c"), TextBoxSolucion.get("1.0", "end-1c"), comboN.get()] 
    
    campos_con_labels = [f"{label}{valor}"  for label, valor in zip(labels, valores)]
    
    campos_str = "\n".join(campos_con_labels)
    pyperclip.copy(campos_str)
    print("Campos copiados al portapapeles.")
   

def limpiar_campos():
    
    TextBoxId.delete(0, END)
    TextBoxNombre.delete(0, END)
    TextBoxTelefono.delete(0, END)
    comboP.set('')
    comboF.set('')
    TextBoxFalla.delete("1.0", "end-1c")
    TextBoxSolucion.delete("1.0", "end-1c")
    comboN.set('')     

def ActualizarTabla():
    actualizarTreeView()
    
    grafica_Tier()
    messagebox.showinfo("Informacion","Tabla actualizada")
    

def obtener_datos_reporte():
    try:
        datos_reporte = []

        # Obtener todos los elementos del TreeView
        items = tree.get_children()

        for item in items:
            # Obtener los valores de cada fila
            values = tree.item(item, 'values')
            datos_reporte.append(values)

        return datos_reporte
    except Exception as e:
        print("Error al obtener datos del reporte:", e)
        return []

def guardar_reporte():
    try:
        datos_reporte = obtener_datos_reporte()

        if not datos_reporte:
            messagebox.showerror("Error", "No hay datos para guardar.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx"), ("Todos los archivos", "*.*")],
            title="Guardar reporte"
        )

        if file_path:
            file_extension = os.path.splitext(file_path)[1].lower()

            if file_extension in ['.csv', '.xlsx']:
                if file_extension == '.csv':
                    guardar_csv(file_path, datos_reporte)
                elif file_extension == '.xlsx':
                    guardar_xlsx(file_path, datos_reporte)
            else:
                messagebox.showerror("Error", "Formato de archivo no válido. Por favor, seleccione un formato compatible (.csv o .xlsx)")
        else:
            print("Guardado cancelado por el usuario")
    except Exception as e:
        print("Error al guardar el reporte:", e)

def guardar_csv(file_path, datos_reporte):
    with open(file_path, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "NOMBRE", "TELEFONO", "PUEBLO", "FINANCIAMIENTO", "FALLA DEL CLIENTE", "SOPORTE BRINDADO", "TIER 1"])
        writer.writerows(datos_reporte)
        messagebox.showinfo("Informacion","Reporte CSV guardado correctamente")

def guardar_xlsx(file_path, datos_reporte):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.append(["ID", "NOMBRE", "TELEFONO", "PUEBLO", "FINANCIAMIENTO", "FALLA DEL CLIENTE", "SOPORTE BRINDADO", "TIER 1"])
    for row in datos_reporte:
        sheet.append(row)
    workbook.save(file_path)
    messagebox.showinfo("Informacion","Reporte EXCEL guardado correctamente")
        
        
def buscar_cliente():
    criterio_busqueda = comboBuscarPor.get()
    valor_busqueda = TextBoxValorBusqueda.get("1.0", "end-1c")

    if not valor_busqueda:
        messagebox.showwarning("Advertencia", "Por favor ingrese un valor para la búsqueda.")
        return

    cliente = CClientes()
    resultados = cliente.BuscarCliente(criterio_busqueda, valor_busqueda)

    if resultados:
        tree.delete(*tree.get_children())  # Limpiar tabla antes de mostrar resultados

        for row in resultados:
            tree.insert("", "end", values=row)
            
        messagebox.showinfo("Información", "Busqueda exitosa.")    
        TextBoxValorBusqueda.delete("1.0", "end-1c")
    else:
        messagebox.showinfo("Información", "No se encontraron resultados para la búsqueda.")
    
         
formulario = FormularioClientes()
Formulario()