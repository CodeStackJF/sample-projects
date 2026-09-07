from conexion_db import conectar

class UsuarioDatabase:
    def __init__(self):
        self.conexion = conectar()

    """ def guardar(self, nombre, apellido, correo):
        cursor = self.conexion.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, apellido, correo) VALUES (?, ?, ?)", 
                       (nombre, apellido, correo))
        self.conexion.commit() """

    def guardar(self, usuario):
        cursor = self.conexion.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, apellido, correo) VALUES (?, ?, ?)", 
                       (usuario.nombre, usuario.apellido, usuario.correo))
        self.conexion.commit()

    def leerUsuarios(self):
        cursor = self.conexion.cursor()
        usuarios = cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        return usuarios

    def correoExiste(self, id, correo):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT 1 FROM usuarios WHERE id != ? AND correo = ?", (id, correo))
        resultado = cursor.fetchone()
        return bool(resultado[0]) if resultado else False

    def leerUsuario(self, id):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
        usuario = cursor.fetchone()
        return usuario

    def actualizar(self, usuario):
        cursor = self.conexion.cursor()
        cursor.execute("UPDATE usuarios SET nombre = ?, apellido = ?, correo = ? WHERE id = ?", 
                       (usuario.nombre, usuario.apellido, usuario.correo, usuario.id))        

    def eliminar(self, id):
        cursor = self.conexion.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (id, ))