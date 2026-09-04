from typing import Any

from db_connection import connect

class UserDatabase:
    def __init__(self) -> None:
        self.conn = connect()

    def save(self, user) -> None:
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO users (first_name, last_name, email) VALUES (?, ?, ?)", 
                       (user.first_name, user.last_name, user.email))
        self.conn.commit()
        
    def close(self) -> None:
        self.conn.close()
        
    def getAll(self) -> list[Any]:
        cursor = self.conn.cursor()
        users = cursor.execute("SELECT * FROM users")
        users = users.fetchall()
        return users
    
    def get(self, userId) -> list[Any]:
            cursor = self.conn.cursor()
            user = cursor.execute("SELECT * FROM users where id = ?", (userId,))
            user = user.fetchone()
            return user
    
    def delete(self, id) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", id)
        self.conn.commit()
        return cursor.rowcount > 0
    
    def update(self, id, user) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("UPDATE users SET first_name = ?, last_name = ?, email = ? WHERE id = ?", (user.first_name, user.last_name, user.email, id))
        return cursor.rowcount > 0
    
    def emailExists(self, id, email)-> bool:
        cursor = self.conn.cursor()
        cursor.execute("SELECT 1 FROM users WHERE id != ? AND email = ?", (id, email))
        result = cursor.fetchone()
        return bool(result[0]) if result else False