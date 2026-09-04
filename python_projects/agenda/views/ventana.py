import tkinter as tk
from tkinter import messagebox

from models.persona import Persona
from controllers.persona_controller import PersonaController


class Aplicacion(tk.Tk):

    def __init__(self):

        super().__init__()

        self.title("Personas")
        self.geometry("400x450")

        self.controller = PersonaController()

        self.persona_id = None

        self.crear_variables()
        self.crear_interfaz()

    def crear_variables(self):

        self.nombre = tk.StringVar()
        self.apellido = tk.StringVar()
        self.email = tk.StringVar()

        self.telefono = tk.StringVar()

    def crear_interfaz(self):

        tk.Label(
            self,
            text="DATOS DE LA PERSONA",
            font=("Arial", 14)
        ).pack(pady=15)

        # Nombre

        tk.Label(
            self,
            text="Nombre:"
        ).pack(anchor="w", padx=20)

        tk.Entry(
            self,
            textvariable=self.nombre
        ).pack(
            fill="x",
            padx=20,
            pady=5
        )

        # Apellido

        tk.Label(
            self,
            text="Apellido:"
        ).pack(anchor="w", padx=20)

        tk.Entry(
            self,
            textvariable=self.apellido
        ).pack(
            fill="x",
            padx=20,
            pady=5
        )

        # Email

        tk.Label(
            self,
            text="Correo:"
        ).pack(anchor="w", padx=20)

        tk.Entry(
            self,
            textvariable=self.email
        ).pack(
            fill="x",
            padx=20,
            pady=5
        )

        # Teléfono

        tk.Label(
            self,
            text="Teléfono:"
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 0)
        )

        frame_telefono = tk.Frame(self)

        frame_telefono.pack(
            fill="x",
            padx=20
        )

        tk.Entry(
            frame_telefono,
            textvariable=self.telefono
        ).pack(
            side="left",
            fill="x",
            expand=True
        )

        tk.Button(
            frame_telefono,
            text="Agregar",
            command=self.agregar_telefono
        ).pack(
            side="right",
            padx=(5, 0)
        )

        # Lista teléfonos

        tk.Label(
            self,
            text="Teléfonos:"
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 5)
        )

        self.lista_telefonos = tk.Listbox(
            self,
            height=6
        )

        self.lista_telefonos.pack(
            fill="x",
            padx=20
        )

        # Guardar

        tk.Button(
            self,
            text="Guardar persona",
            command=self.guardar
        ).pack(
            pady=20
        )

    def agregar_telefono(self):

        telefono = self.telefono.get().strip()

        if not telefono:
            messagebox.showwarning(
                "Teléfono",
                "Ingrese un número."
            )
            return

        self.lista_telefonos.insert(
            tk.END,
            telefono
        )

        self.telefono.set("")

    def guardar(self):

        nombre = self.nombre.get().strip()
        apellido = self.apellido.get().strip()
        email = self.email.get().strip()

        if not nombre or not apellido:

            messagebox.showwarning(
                "Datos",
                "Nombre y apellido son obligatorios."
            )

            return

        persona = Persona(
            nombre,
            apellido,
            email
        )

        persona_id = self.controller.guardar_persona(
            persona
        )

        # Guardar todos los teléfonos

        for telefono in self.lista_telefonos.get(0, tk.END):

            self.controller.guardar_telefono(
                persona_id,
                telefono
            )

        messagebox.showinfo(
            "Correcto",
            "Persona guardada correctamente."
        )

        self.limpiar()

    def limpiar(self):

        self.nombre.set("")
        self.apellido.set("")
        self.email.set("")
        self.telefono.set("")

        self.lista_telefonos.delete(
            0,
            tk.END
        )