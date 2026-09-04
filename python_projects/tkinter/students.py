import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime


# ============================================================
# BASE DE DATOS
# ============================================================

DB_NAME = "expedientes.db"


def conectar():
    return sqlite3.connect(DB_NAME)


def crear_base_datos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estudiantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT UNIQUE NOT NULL,
            nombres TEXT NOT NULL,
            apellidos TEXT NOT NULL,
            fecha_nacimiento TEXT,
            genero TEXT,
            telefono TEXT,
            email TEXT,
            direccion TEXT,
            grado TEXT,
            seccion TEXT,
            anio TEXT,
            encargado TEXT,
            telefono_encargado TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS eventos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            estudiante_id INTEGER NOT NULL,
            fecha TEXT NOT NULL,
            tipo TEXT NOT NULL,
            descripcion TEXT,
            observaciones TEXT,
            FOREIGN KEY (estudiante_id)
                REFERENCES estudiantes(id)
                ON DELETE CASCADE
        )
    """)

    conn.commit()
    conn.close()


# ============================================================
# FUNCIONES
# ============================================================

def limpiar_campos():
    codigo_var.set("")
    nombres_var.set("")
    apellidos_var.set("")
    nacimiento_var.set("")
    genero_var.set("")
    telefono_var.set("")
    email_var.set("")
    direccion_var.set("")
    grado_var.set("")
    seccion_var.set("")
    anio_var.set("")
    encargado_var.set("")
    telefono_encargado_var.set("")

    estudiante_id_var.set("")

    for item in tabla_eventos.get_children():
        tabla_eventos.delete(item)

    fecha_evento_var.set(datetime.now().strftime("%Y-%m-%d"))
    tipo_evento_var.set("")
    descripcion_var.set("")
    observaciones_var.set("")


def guardar_estudiante():
    codigo = codigo_var.get().strip()
    nombres = nombres_var.get().strip()
    apellidos = apellidos_var.get().strip()

    if not codigo or not nombres or not apellidos:
        messagebox.showwarning(
            "Datos incompletos",
            "Debe ingresar código, nombres y apellidos."
        )
        return

    datos = (
        codigo,
        nombres,
        apellidos,
        nacimiento_var.get(),
        genero_var.get(),
        telefono_var.get(),
        email_var.get(),
        direccion_var.get(),
        grado_var.get(),
        seccion_var.get(),
        anio_var.get(),
        encargado_var.get(),
        telefono_encargado_var.get()
    )

    conn = conectar()
    cursor = conn.cursor()

    try:
        if estudiante_id_var.get():
            cursor.execute("""
                UPDATE estudiantes SET
                    codigo=?,
                    nombres=?,
                    apellidos=?,
                    fecha_nacimiento=?,
                    genero=?,
                    telefono=?,
                    email=?,
                    direccion=?,
                    grado=?,
                    seccion=?,
                    anio=?,
                    encargado=?,
                    telefono_encargado=?
                WHERE id=?
            """, datos + (estudiante_id_var.get(),))

            mensaje = "Expediente actualizado correctamente."

        else:
            cursor.execute("""
                INSERT INTO estudiantes (
                    codigo, nombres, apellidos,
                    fecha_nacimiento, genero,
                    telefono, email, direccion,
                    grado, seccion, anio,
                    encargado, telefono_encargado
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, datos)

            estudiante_id_var.set(cursor.lastrowid)

            mensaje = "Expediente guardado correctamente."

        conn.commit()

        cargar_estudiantes()

        messagebox.showinfo("Éxito", mensaje)

    except sqlite3.IntegrityError:
        messagebox.showerror(
            "Error",
            "El código del estudiante ya existe."
        )

    finally:
        conn.close()


def cargar_estudiantes():
    for item in tabla_estudiantes.get_children():
        tabla_estudiantes.delete(item)

    conn = conectar()
    cursor = conn.cursor()

    texto = buscar_var.get().strip()

    if texto:
        cursor.execute("""
            SELECT id, codigo, nombres, apellidos,
                   grado, seccion
            FROM estudiantes
            WHERE codigo LIKE ?
               OR nombres LIKE ?
               OR apellidos LIKE ?
            ORDER BY apellidos, nombres
        """, (
            f"%{texto}%",
            f"%{texto}%",
            f"%{texto}%"
        ))
    else:
        cursor.execute("""
            SELECT id, codigo, nombres, apellidos,
                   grado, seccion
            FROM estudiantes
            ORDER BY apellidos, nombres
        """)

    estudiantes = cursor.fetchall()

    for estudiante in estudiantes:
        tabla_estudiantes.insert(
            "",
            "end",
            values=estudiante
        )

    conn.close()


def seleccionar_estudiante(event=None):
    seleccionado = tabla_estudiantes.selection()

    if not seleccionado:
        return

    item = tabla_estudiantes.item(seleccionado[0])
    estudiante_id = item["values"][0]

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM estudiantes
        WHERE id=?
    """, (estudiante_id,))

    estudiante = cursor.fetchone()
    conn.close()

    if estudiante:
        estudiante_id_var.set(estudiante[0])
        codigo_var.set(estudiante[1])
        nombres_var.set(estudiante[2])
        apellidos_var.set(estudiante[3])
        nacimiento_var.set(estudiante[4])
        genero_var.set(estudiante[5])
        telefono_var.set(estudiante[6])
        email_var.set(estudiante[7])
        direccion_var.set(estudiante[8])
        grado_var.set(estudiante[9])
        seccion_var.set(estudiante[10])
        anio_var.set(estudiante[11])
        encargado_var.set(estudiante[12])
        telefono_encargado_var.set(estudiante[13])

        cargar_eventos(estudiante_id)


def cargar_eventos(estudiante_id):
    for item in tabla_eventos.get_children():
        tabla_eventos.delete(item)

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, fecha, tipo, descripcion, observaciones
        FROM eventos
        WHERE estudiante_id=?
        ORDER BY fecha DESC, id DESC
    """, (estudiante_id,))

    eventos = cursor.fetchall()

    for evento in eventos:
        tabla_eventos.insert(
            "",
            "end",
            values=evento
        )

    conn.close()


def agregar_evento():
    estudiante_id = estudiante_id_var.get()

    if not estudiante_id:
        messagebox.showwarning(
            "Estudiante",
            "Primero debe guardar o seleccionar un estudiante."
        )
        return

    fecha = fecha_evento_var.get().strip()
    tipo = tipo_evento_var.get().strip()
    descripcion = descripcion_var.get().strip()
    observaciones = observaciones_var.get().strip()

    if not fecha or not tipo:
        messagebox.showwarning(
            "Datos incompletos",
            "Ingrese la fecha y el tipo de evento."
        )
        return

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO eventos (
            estudiante_id,
            fecha,
            tipo,
            descripcion,
            observaciones
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        estudiante_id,
        fecha,
        tipo,
        descripcion,
        observaciones
    ))

    conn.commit()
    conn.close()

    cargar_eventos(estudiante_id)

    descripcion_var.set("")
    observaciones_var.set("")

    messagebox.showinfo(
        "Evento",
        "Evento agregado correctamente."
    )


def eliminar_evento():
    seleccionado = tabla_eventos.selection()

    if not seleccionado:
        messagebox.showwarning(
            "Evento",
            "Seleccione un evento."
        )
        return

    item = tabla_eventos.item(seleccionado[0])
    evento_id = item["values"][0]

    confirmar = messagebox.askyesno(
        "Confirmar",
        "¿Desea eliminar este evento?"
    )

    if not confirmar:
        return

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM eventos WHERE id=?",
        (evento_id,)
    )

    conn.commit()
    conn.close()

    cargar_eventos(estudiante_id_var.get())


def mostrar_evento(event=None):
    seleccionado = tabla_eventos.selection()

    if not seleccionado:
        return

    item = tabla_eventos.item(seleccionado[0])
    valores = item["values"]

    fecha_evento_var.set(valores[1])
    tipo_evento_var.set(valores[2])
    descripcion_var.set(valores[3])
    observaciones_var.set(valores[4])


def buscar_estudiantes(*args):
    cargar_estudiantes()


# ============================================================
# VENTANA PRINCIPAL
# ============================================================

crear_base_datos()

root = tk.Tk()
root.title("Sistema de Expedientes Estudiantiles")
root.geometry("1250x750")
root.minsize(1050, 650)

# ============================================================
# VARIABLES
# ============================================================

estudiante_id_var = tk.StringVar()

codigo_var = tk.StringVar()
nombres_var = tk.StringVar()
apellidos_var = tk.StringVar()
nacimiento_var = tk.StringVar()
genero_var = tk.StringVar()
telefono_var = tk.StringVar()
email_var = tk.StringVar()
direccion_var = tk.StringVar()
grado_var = tk.StringVar()
seccion_var = tk.StringVar()
anio_var = tk.StringVar()
encargado_var = tk.StringVar()
telefono_encargado_var = tk.StringVar()

buscar_var = tk.StringVar()

fecha_evento_var = tk.StringVar(
    value=datetime.now().strftime("%Y-%m-%d")
)
tipo_evento_var = tk.StringVar()
descripcion_var = tk.StringVar()
observaciones_var = tk.StringVar()

buscar_var.trace_add("write", buscar_estudiantes)


# ============================================================
# ESTILOS
# ============================================================

style = ttk.Style()

try:
    style.theme_use("clam")
except tk.TclError:
    pass

style.configure(
    "Titulo.TLabel",
    font=("Segoe UI", 16, "bold")
)

style.configure(
    "Subtitulo.TLabel",
    font=("Segoe UI", 11, "bold")
)

style.configure(
    "TButton",
    font=("Segoe UI", 10)
)

style.configure(
    "Treeview",
    rowheight=28,
    font=("Segoe UI", 9)
)

style.configure(
    "Treeview.Heading",
    font=("Segoe UI", 9, "bold")
)


# ============================================================
# ENCABEZADO
# ============================================================

titulo = ttk.Label(
    root,
    text="EXPEDIENTE ESTUDIANTIL",
    style="Titulo.TLabel"
)

titulo.pack(pady=(15, 5))


# ============================================================
# CONTENEDOR PRINCIPAL
# ============================================================

contenedor = ttk.Frame(root)
contenedor.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=10
)

contenedor.columnconfigure(0, weight=1)
contenedor.columnconfigure(1, weight=2)
contenedor.rowconfigure(0, weight=1)


# ============================================================
# PANEL IZQUIERDO
# ============================================================

panel_izquierdo = ttk.Frame(
    contenedor,
    padding=10
)

panel_izquierdo.grid(
    row=0,
    column=0,
    sticky="nsew"
)

panel_izquierdo.rowconfigure(1, weight=1)


# ------------------------------------------------------------
# BÚSQUEDA
# ------------------------------------------------------------

frame_busqueda = ttk.LabelFrame(
    panel_izquierdo,
    text="Buscar estudiante",
    padding=10
)

frame_busqueda.pack(
    fill="x",
    pady=(0, 10)
)

ttk.Entry(
    frame_busqueda,
    textvariable=buscar_var
).pack(
    fill="x"
)


# ------------------------------------------------------------
# TABLA ESTUDIANTES
# ------------------------------------------------------------

frame_lista = ttk.LabelFrame(
    panel_izquierdo,
    text="Estudiantes registrados",
    padding=5
)

frame_lista.pack(
    fill="both",
    expand=True
)

columnas_estudiantes = (
    "id",
    "codigo",
    "nombres",
    "apellidos",
    "grado",
    "seccion"
)

tabla_estudiantes = ttk.Treeview(
    frame_lista,
    columns=columnas_estudiantes,
    show="headings"
)

tabla_estudiantes.heading("id", text="ID")
tabla_estudiantes.heading("codigo", text="Código")
tabla_estudiantes.heading("nombres", text="Nombres")
tabla_estudiantes.heading("apellidos", text="Apellidos")
tabla_estudiantes.heading("grado", text="Grado")
tabla_estudiantes.heading("seccion", text="Sección")

tabla_estudiantes.column("id", width=45)
tabla_estudiantes.column("codigo", width=90)
tabla_estudiantes.column("nombres", width=120)
tabla_estudiantes.column("apellidos", width=120)
tabla_estudiantes.column("grado", width=70)
tabla_estudiantes.column("seccion", width=60)

scroll_estudiantes = ttk.Scrollbar(
    frame_lista,
    orient="vertical",
    command=tabla_estudiantes.yview
)

tabla_estudiantes.configure(
    yscrollcommand=scroll_estudiantes.set
)

tabla_estudiantes.pack(
    side="left",
    fill="both",
    expand=True
)

scroll_estudiantes.pack(
    side="right",
    fill="y"
)

tabla_estudiantes.bind(
    "<<TreeviewSelect>>",
    seleccionar_estudiante
)


# ============================================================
# PANEL DERECHO
# ============================================================

panel_derecho = ttk.Frame(
    contenedor,
    padding=10
)

panel_derecho.grid(
    row=0,
    column=1,
    sticky="nsew"
)


# ============================================================
# DATOS DEL ESTUDIANTE
# ============================================================

frame_datos = ttk.LabelFrame(
    panel_derecho,
    text="Datos del estudiante",
    padding=10
)

frame_datos.pack(
    fill="x"
)

for columna in range(4):
    frame_datos.columnconfigure(columna, weight=1)


def campo(parent, texto, variable, fila, columna):
    ttk.Label(
        parent,
        text=texto
    ).grid(
        row=fila,
        column=columna,
        sticky="w",
        padx=5,
        pady=4
    )

    ttk.Entry(
        parent,
        textvariable=variable
    ).grid(
        row=fila,
        column=columna + 1,
        sticky="ew",
        padx=5,
        pady=4
    )


campo(frame_datos, "Código:", codigo_var, 0, 0)
campo(frame_datos, "Nombres:", nombres_var, 0, 2)

campo(frame_datos, "Apellidos:", apellidos_var, 1, 0)
campo(frame_datos, "Nacimiento:", nacimiento_var, 1, 2)

campo(frame_datos, "Género:", genero_var, 2, 0)
campo(frame_datos, "Teléfono:", telefono_var, 2, 2)

campo(frame_datos, "Correo:", email_var, 3, 0)
campo(frame_datos, "Dirección:", direccion_var, 3, 2)

campo(frame_datos, "Grado:", grado_var, 4, 0)
campo(frame_datos, "Sección:", seccion_var, 4, 2)

campo(frame_datos, "Año lectivo:", anio_var, 5, 0)
campo(frame_datos, "Encargado:", encargado_var, 5, 2)

campo(
    frame_datos,
    "Tel. encargado:",
    telefono_encargado_var,
    6,
    0
)


# ============================================================
# BOTONES DEL EXPEDIENTE
# ============================================================

frame_botones = ttk.Frame(panel_derecho)
frame_botones.pack(
    fill="x",
    pady=10
)

ttk.Button(
    frame_botones,
    text="Guardar expediente",
    command=guardar_estudiante
).pack(
    side="left",
    padx=5
)

ttk.Button(
    frame_botones,
    text="Nuevo / Limpiar",
    command=limpiar_campos
).pack(
    side="left",
    padx=5
)

ttk.Button(
    frame_botones,
    text="Actualizar lista",
    command=cargar_estudiantes
).pack(
    side="left",
    padx=5
)


# ============================================================
# EVENTOS
# ============================================================

frame_eventos = ttk.LabelFrame(
    panel_derecho,
    text="Eventos del expediente",
    padding=10
)

frame_eventos.pack(
    fill="both",
    expand=True
)


# ------------------------------------------------------------
# FORMULARIO EVENTO
# ------------------------------------------------------------

frame_evento_form = ttk.Frame(frame_eventos)
frame_evento_form.pack(
    fill="x",
    pady=(0, 10)
)

frame_evento_form.columnconfigure(1, weight=1)
frame_evento_form.columnconfigure(3, weight=2)

ttk.Label(
    frame_evento_form,
    text="Fecha:"
).grid(
    row=0,
    column=0,
    padx=5,
    pady=5,
    sticky="w"
)

ttk.Entry(
    frame_evento_form,
    textvariable=fecha_evento_var,
    width=15
).grid(
    row=0,
    column=1,
    padx=5,
    pady=5,
    sticky="w"
)

ttk.Label(
    frame_evento_form,
    text="Tipo:"
).grid(
    row=0,
    column=2,
    padx=5,
    pady=5,
    sticky="w"
)

combo_tipo = ttk.Combobox(
    frame_evento_form,
    textvariable=tipo_evento_var,
    values=[
        "Académico",
        "Conducta",
        "Asistencia",
        "Disciplina",
        "Reunión",
        "Reconocimiento",
        "Salud",
        "Administrativo",
        "Otro"
    ],
    state="readonly"
)

combo_tipo.grid(
    row=0,
    column=3,
    padx=5,
    pady=5,
    sticky="ew"
)

ttk.Label(
    frame_evento_form,
    text="Descripción:"
).grid(
    row=1,
    column=0,
    padx=5,
    pady=5,
    sticky="w"
)

ttk.Entry(
    frame_evento_form,
    textvariable=descripcion_var
).grid(
    row=1,
    column=1,
    columnspan=3,
    padx=5,
    pady=5,
    sticky="ew"
)

ttk.Label(
    frame_evento_form,
    text="Observaciones:"
).grid(
    row=2,
    column=0,
    padx=5,
    pady=5,
    sticky="w"
)

ttk.Entry(
    frame_evento_form,
    textvariable=observaciones_var
).grid(
    row=2,
    column=1,
    columnspan=3,
    padx=5,
    pady=5,
    sticky="ew"
)


# ------------------------------------------------------------
# BOTONES EVENTOS
# ------------------------------------------------------------

frame_evento_botones = ttk.Frame(frame_eventos)
frame_evento_botones.pack(
    fill="x",
    pady=5
)

ttk.Button(
    frame_evento_botones,
    text="Agregar evento",
    command=agregar_evento
).pack(
    side="left",
    padx=5
)

ttk.Button(
    frame_evento_botones,
    text="Eliminar evento",
    command=eliminar_evento
).pack(
    side="left",
    padx=5
)


# ------------------------------------------------------------
# TABLA EVENTOS
# ------------------------------------------------------------

frame_tabla_eventos = ttk.Frame(frame_eventos)
frame_tabla_eventos.pack(
    fill="both",
    expand=True
)

columnas_eventos = (
    "id",
    "fecha",
    "tipo",
    "descripcion",
    "observaciones"
)

tabla_eventos = ttk.Treeview(
    frame_tabla_eventos,
    columns=columnas_eventos,
    show="headings"
)

tabla_eventos.heading("id", text="ID")
tabla_eventos.heading("fecha", text="Fecha")
tabla_eventos.heading("tipo", text="Tipo")
tabla_eventos.heading("descripcion", text="Descripción")
tabla_eventos.heading("observaciones", text="Observaciones")

tabla_eventos.column("id", width=40)
tabla_eventos.column("fecha", width=90)
tabla_eventos.column("tipo", width=110)
tabla_eventos.column("descripcion", width=250)
tabla_eventos.column("observaciones", width=250)

scroll_eventos = ttk.Scrollbar(
    frame_tabla_eventos,
    orient="vertical",
    command=tabla_eventos.yview
)

tabla_eventos.configure(
    yscrollcommand=scroll_eventos.set
)

tabla_eventos.pack(
    side="left",
    fill="both",
    expand=True
)

scroll_eventos.pack(
    side="right",
    fill="y"
)

tabla_eventos.bind(
    "<<TreeviewSelect>>",
    mostrar_evento
)


# ============================================================
# INICIO
# ============================================================

cargar_estudiantes()

root.mainloop()