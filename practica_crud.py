from tkinter import *
from tkinter import messagebox
import sqlite3


root = Tk()
root.geometry("350x400")
cuadro = Frame(root)
cuadro.pack()
cuadro_de_botones = Frame(root)
cuadro_de_botones.pack()

def conectar():
    try:
        conexion = sqlite3.connect("Usuarios")
        conexion.execute("""CREATE TABLE DATOSUSUARIOS (
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            NOMBRE_USUARIO VARCHAR(50),
                            PASSWORD VARCHAR(50),
                            APELLIDO VARCHAR(10),
                            DIRECCION VARCHAR(50),
                            COMENTARIOS VARCHAR(100)
                            )"""
                            )
        messagebox.showinfo("BBDD", "BBDD creada con éxito")
    except sqlite3.OperationalError:
        messagebox.showwarning("Atención!", "La base de datos ya existe")        

def salir():
    respuesta = messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")
    if respuesta == "yes":
        root.destroy()  

def borrar_campos():
    entries.id_entry.delete(0, END)
    entries.nombre_entry.delete(0, END)
    entries.pass_entry.delete(0, END)
    entries.apellido_entry.delete(0, END)
    entries.direccion_entry.delete(0, END)
    comentario.comentario_text.delete(1.0, END)
    
def crear():
    conexion = sqlite3.connect("Usuarios")
    cursor = conexion.cursor()
    datos = [entries.nombre_entry.get(), entries.pass_entry.get(), entries.apellido_entry.get(), entries.direccion_entry.get(), comentario.comentario_text.get(1.0, END)]
    cursor.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL, ?, ?, ?, ?, ?)", datos)
    """cursor.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL, '" + 
        entries.nombre_entry.get() + "','" + 
        entries.pass_entry.get() + "','" + 
        entries.apellido_entry.get() + "','" + 
        entries.direccion_entry.get() + "','" + 
        comentario.comentario_text.get(1.0, END) + "')")"""
    conexion.commit()
    borrar_campos()
    messagebox.showinfo("BBDD", "Registro guardado con éxito")

def leer():
    # Read from database Usuarios using ID
    conexion = sqlite3.connect("Usuarios")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID = " + entries.id_entry.get())
    usuario = cursor.fetchone()
    entries.nombre_entry.insert(0, usuario[1])
    entries.pass_entry.insert(0, usuario[2])
    entries.apellido_entry.insert(0, usuario[3])
    entries.direccion_entry.insert(0, usuario[4])
    comentario.comentario_text.insert(1.0, usuario[5])
    
def actualizar():
    # Update in database Usuarios
    conexion = sqlite3.connect("Usuarios")
    cursor = conexion.cursor()
    cursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO = '" + entries.nombre_entry.get() + 
        "', PASSWORD = '" + entries.pass_entry.get() + 
        "', APELLIDO = '" + entries.apellido_entry.get() + 
        "', DIRECCION = '" + entries.direccion_entry.get() + 
        "', COMENTARIOS = '" + comentario.comentario_text.get(1.0, END) + 
        "' WHERE ID = " + entries.id_entry.get())
    conexion.commit()
    borrar_campos()
    messagebox.showinfo("BBDD", "Registro actualizado con éxito")


def borrar():
    # Delete from database Usuarios
    conexion = sqlite3.connect("Usuarios")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID = " + entries.id_entry.get())
    conexion.commit()
    borrar_campos()
    messagebox.showinfo("BBDD", "Registro borrado con éxito")

def licencia():
    pass    

def acerca():
    pass    


class BBDD:
    def __init__(self):
        self.conexion = sqlite3.connect("Usuarios")
        self.cursor = self.conexion.cursor()
        

class BarraMenu:
    def __init__(self):
        self.barra_menu = Menu(root)
        root.config(menu=self.barra_menu)

        self.bbdd = Menu(self.barra_menu, tearoff=0)
        self.bbdd.add_command(label="Conectar", command=conectar)    
        self.bbdd.add_command(label="Salir", command=salir)

        self.borrar = Menu(self.barra_menu, tearoff=0)
        self.borrar.add_command(label="Borrar campos", command=borrar_campos)

        self.crud = Menu(self.barra_menu, tearoff=0)
        self.crud.add_command(label="Crear", command=crear)
        self.crud.add_command(label="Leer", command=leer)
        self.crud.add_command(label="Actualizar", command=actualizar)
        self.crud.add_command(label="Borrar", command=borrar)

        self.ayuda = Menu(self.barra_menu, tearoff=0)
        self.ayuda.add_command(label="Licencia", command=licencia)
        self.ayuda.add_command(label="Acerca de...", command=acerca)
        
        self.barra_menu.add_cascade(label="BBDD", menu=self.bbdd)
        self.barra_menu.add_cascade(label="Ayuda", menu=self.ayuda)
        self.barra_menu.add_cascade(label="Borrar", menu=self.borrar)
        self.barra_menu.add_cascade(label="CRUD", menu=self.crud)


class Entries:
    def __init__(self):
        # Lista de entries y text variables
        id = StringVar()
        self.id_entry = Entry(cuadro, textvariable=id)
        self.id_entry.grid(row=0, column=1, padx=10, pady=10)
        self.id_label = Label(cuadro, text="Id: ")
        self.id_label.grid(row=0, column=0, sticky=E, padx=10, pady=10)

        nombre = StringVar()
        self.nombre_entry = Entry(cuadro, textvariable=nombre)
        self.nombre_entry.grid(row=1, column=1, padx=10, pady=10)
        self.nombre_entry.config(fg="red", justify="right")
        self.nombre_label = Label(cuadro, text="Nombre: ")
        self.nombre_label.grid(row=1, column=0, sticky=E, padx=10, pady=10)

        password = StringVar()
        self.pass_entry = Entry(cuadro, textvariable=password)
        self.pass_entry.grid(row=2, column=1, padx=10, pady=10)
        self.pass_entry.config(show="*")
        self.pass_label = Label(cuadro, text="Password: ")
        self.pass_label.grid(row=2, column=0, sticky=E, padx=10, pady=10)

        apellido = StringVar()
        self.apellido_entry = Entry(cuadro, textvariable=apellido)
        self.apellido_entry.grid(row=3, column=1, padx=10, pady=10)
        self.apellido_label = Label(cuadro, text="Apellido: ")
        self.apellido_label.grid(row=3, column=0, sticky=E, padx=10, pady=10)   

        direccion = StringVar()
        self.direccion_entry = Entry(cuadro, textvariable=direccion)
        self.direccion_entry.grid(row=4, column=1, padx=10, pady=10)
        self.direccion_label = Label(cuadro, text="Dirección: ")
        self.direccion_label.grid(row=4, column=0, sticky=E, padx=10, pady=10)

        
class Comentarios:
    def __init__(self):
        self.comentario_label = Label(cuadro, text="Comentarios: ")
        self.comentario_label.grid(row=5, column=0, sticky=E, padx=10, pady=10)
        self.comentario_text = Text(cuadro, width=20, height=5)
        self.comentario_text.grid(row=5, column=1, padx=10, pady=10)
        self.barra_de_scroll = Scrollbar(cuadro, command=self.comentario_text.yview)
        self.barra_de_scroll.grid(row=5, column=2, sticky="nsew")
        self.comentario_text.config(yscrollcommand=self.barra_de_scroll.set)


class Botones:
    def __init__(self):
        create_button = Button(cuadro_de_botones, text="Create", command=crear)
        create_button.grid(row=0, column=0, padx=10, pady=10)
        read_button = Button(cuadro_de_botones, text="Read", command=leer)
        read_button.grid(row=0, column=1, padx=10, pady=10)
        update_button = Button(cuadro_de_botones, text="Update", command=actualizar)
        update_button.grid(row=0, column=2, padx=10, pady=10)
        delete_button = Button(cuadro_de_botones, text="Delete", command=borrar)
        delete_button.grid(row=0, column=3, padx=10, pady=10)

        
menus = BarraMenu()        
entries = Entries()
comentario = Comentarios()
botones = Botones()



root.mainloop()
