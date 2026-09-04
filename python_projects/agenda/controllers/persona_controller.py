from database.database import conectar


class PersonaController:

    def guardar_persona(self, persona):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO personas (
                nombre,
                apellido,
                email
            )
            VALUES (?, ?, ?)
        """, (
            persona.nombre,
            persona.apellido,
            persona.email
        ))

        persona_id = cursor.lastrowid

        conn.commit()
        conn.close()

        return persona_id

    def guardar_telefono(
        self,
        persona_id,
        telefono
    ):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO telefonos (
                persona_id,
                telefono
            )
            VALUES (?, ?)
        """, (
            persona_id,
            telefono
        ))

        conn.commit()
        conn.close()

    def obtener_telefonos(
        self,
        persona_id
    ):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, telefono
            FROM telefonos
            WHERE persona_id = ?
            ORDER BY id
        """, (persona_id,))

        telefonos = cursor.fetchall()

        conn.close()

        return telefonos