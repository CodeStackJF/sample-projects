import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from usuariosRepository import UsuarioDatabase
from entidades.usuario import Usuario

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mi primera conexión a base de datos")
        self.geometry("800x600")
        self.usuarioDatabase = UsuarioDatabase()
        

    def crearVariables(self):
        self.id = tk.IntVar()
        self.nombre = tk.StringVar()
        self.apellido = tk.StringVar()
        self.correo = tk.StringVar()

    def crearInterfaz(self):

        self.labelID = tk.Label(self, text = "ID")
        self.labelID.grid(row=0, column=0, padx=10)

        self.entryID = tk.Entry(self, textvariable=self.id, state="disabled")
        self.entryID.grid(row=0, column=1, padx=10)

        self.labelNombre = tk.Label(self, text = "Nombre")
        self.labelNombre.grid(row=0, column=2, padx=10)

        self.entryNombre = tk.Entry(self, textvariable=self.nombre)
        self.entryNombre.grid(row=0, column=3, padx=10)

        self.labelApellido = tk.Label(self, text = "Apellido")
        self.labelApellido.grid(row=1, column=0, padx=10)

        self.entryApellido = tk.Entry(self, textvariable=self.apellido)
        self.entryApellido.grid(row=1, column=1, pady=15, padx=10)

        self.labelCorreo = tk.Label(self, text = "Correo")
        self.labelCorreo.grid(row=1, column=2, padx=10)

        self.entryCorreo = tk.Entry(self, textvariable=self.correo)
        self.entryCorreo.grid(row=1, column=3, padx=10)

        self.btnGuardar = tk.Button(text="Aceptar", bg="#111", fg="#fff", width=30, command=self.guardarUsuario)
        self.btnGuardar.grid(row=2, column=0, columnspan=2, pady=15, padx=10)

        self.btnCancelar = tk.Button(text="Cancelar", bg="#111", fg="#fff", width=30, command=self.limpiarCampos)
        self.btnCancelar.grid(row=2, column=2, columnspan=2, pady=15, padx=10)

        columnas = ('id', 'nombre', 'apellido', 'correo')
        self.tablaUsuarios = ttk.Treeview(self, columns=columnas, show="headings",selectmode="browse")

        self.tablaUsuarios.heading("id", text="ID")
        self.tablaUsuarios.heading("nombre", text="Nombre")
        self.tablaUsuarios.heading("apellido", text="Apellido")
        self.tablaUsuarios.heading("correo", text="Correo")

        self.tablaUsuarios.column('id', width=20, anchor="center")
        self.tablaUsuarios.column('nombre', width=150, anchor="center")
        self.tablaUsuarios.column('apellido', width=150, anchor="center")
        self.tablaUsuarios.column('correo', width=150, anchor="center")
        self.tablaUsuarios.bind("<Double-1>", self.editarUsuario)

        self.tablaUsuarios.grid(row=4, column=0, columnspan=4)

        self.btnEliminar = tk.Button(text="Eliminar", bg="#111", fg="#fff", width=30, command=self.eliminarUsuario)
        self.btnEliminar.grid(row=5, column=1, columnspan=2, pady=15, padx=10)

    def mostrarVariables(self):
        messagebox.showwarning("Valores de las variables", self.nombre.get())

    def limpiarCampos(self):
        self.id.set(0)
        self.nombre.set("")
        self.apellido.set("")
        self.correo.set("")
        self.btnGuardar.config(text="Guardar")

    def guardarUsuario(self):
        id = self.id.get()
        nombre = self.nombre.get()
        apellido = self.apellido.get()
        correo = self.correo.get()

        usuario = Usuario(
            id,
            nombre,
            apellido,
            correo
        )

        print(usuario.id)

        if(self.usuarioDatabase.correoExiste(usuario.id, correo)):
                    messagebox.showwarning("Correo existe", "Ya existe un usuario con este correo")
                    return

        #self.usuarioDatabase.guardar(nombre, apellido, correo)
        if usuario.id == 0:
            self.usuarioDatabase.guardar(usuario)
        else:
            self.usuarioDatabase.actualizar(usuario)       
        
        self.cargarUsuarios()
        self.limpiarCampos()

    def cargarUsuarios(self):
        for fila in self.tablaUsuarios.get_children():
            self.tablaUsuarios.delete(fila)

        usuarios = self.usuarioDatabase.leerUsuarios()
        for usuario in usuarios:
            self.tablaUsuarios.insert("", tk.END, values=usuario)

    def editarUsuario(self, event):
        selected = self.tablaUsuarios.focus()
        fila = self.tablaUsuarios.item(selected)
        valores = fila.get("values")
        #print(valores)
        id = valores[0]
        #print(id)
        usuario = self.usuarioDatabase.leerUsuario(id)
        self.id.set(usuario[0])
        self.nombre.set(usuario[1])
        self.apellido.set(usuario[2])
        self.correo.set(usuario[3])
        self.btnGuardar.config(text="Actualizar")

    def eliminarUsuario(self):
        selected = self.tablaUsuarios.focus()
        fila = self.tablaUsuarios.item(selected)
        valores = fila.get("values")
        #print(valores)
        id = valores[0]
        self.usuarioDatabase.eliminar(id)
        self.tablaUsuarios.delete(selected)