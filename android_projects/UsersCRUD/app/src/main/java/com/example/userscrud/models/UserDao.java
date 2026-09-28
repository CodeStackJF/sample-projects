package com.example.userscrud.models;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteConstraintException;
import android.database.sqlite.SQLiteDatabase;

import com.example.userscrud.config.DatabaseHelper;

import java.util.ArrayList;
import java.util.List;

/**
 * Equivalente a models/userModel.js: contiene todas las consultas SQL
 * (crear, leer, actualizar, eliminar) sobre la tabla users.
 */
public class UserDao {

    private final DatabaseHelper dbHelper;

    public UserDao(Context context) {
        this.dbHelper = DatabaseHelper.getInstance(context);
    }

    /** Envuelve el resultado de crear/actualizar, incluyendo el mensaje de error si aplica. */
    public static class Result {
        public final boolean success;
        public final String errorMessage;

        Result(boolean success, String errorMessage) {
            this.success = success;
            this.errorMessage = errorMessage;
        }
    }

    /** Obtiene todos los usuarios, ordenados del más reciente al más antiguo. */
    public List<User> getAllUsers() {
        List<User> users = new ArrayList<>();
        SQLiteDatabase db = dbHelper.getReadableDatabase();
        Cursor cursor = db.query(
                DatabaseHelper.TABLE_USERS,
                null,
                null,
                null,
                null,
                null,
                DatabaseHelper.COLUMN_ID + " DESC"
        );

        if (cursor != null) {
            while (cursor.moveToNext()) {
                users.add(cursorToUser(cursor));
            }
            cursor.close();
        }
        return users;
    }

    /** Obtiene un usuario por su id, o null si no existe. */
    public User getUserById(long id) {
        SQLiteDatabase db = dbHelper.getReadableDatabase();
        Cursor cursor = db.query(
                DatabaseHelper.TABLE_USERS,
                null,
                DatabaseHelper.COLUMN_ID + " = ?",
                new String[]{String.valueOf(id)},
                null,
                null,
                null
        );

        User user = null;
        if (cursor != null) {
            if (cursor.moveToFirst()) {
                user = cursorToUser(cursor);
            }
            cursor.close();
        }
        return user;
    }

    /** Crea un nuevo usuario. Si el email ya existe, devuelve un Result con success=false. */
    public Result insertUser(User user) {
        SQLiteDatabase db = dbHelper.getWritableDatabase();
        ContentValues values = buildContentValues(user);
        try {
            long id = db.insertOrThrow(DatabaseHelper.TABLE_USERS, null, values);
            return new Result(id != -1, id != -1 ? null : "No se pudo crear el usuario");
        } catch (SQLiteConstraintException e) {
            return new Result(false, "El email ya está registrado por otro usuario");
        }
    }

    /** Actualiza un usuario existente. Si el nuevo email ya lo usa otro usuario, falla. */
    public Result updateUser(User user) {
        SQLiteDatabase db = dbHelper.getWritableDatabase();
        ContentValues values = buildContentValues(user);
        try {
            int rows = db.update(
                    DatabaseHelper.TABLE_USERS,
                    values,
                    DatabaseHelper.COLUMN_ID + " = ?",
                    new String[]{String.valueOf(user.getId())}
            );
            return new Result(rows > 0, rows > 0 ? null : "No se pudo actualizar el usuario");
        } catch (SQLiteConstraintException e) {
            return new Result(false, "El email ya está registrado por otro usuario");
        }
    }

    /** Elimina un usuario por id. Devuelve true si se eliminó alguna fila. */
    public boolean deleteUser(long id) {
        SQLiteDatabase db = dbHelper.getWritableDatabase();
        int rows = db.delete(
                DatabaseHelper.TABLE_USERS,
                DatabaseHelper.COLUMN_ID + " = ?",
                new String[]{String.valueOf(id)}
        );
        return rows > 0;
    }

    private ContentValues buildContentValues(User user) {
        ContentValues values = new ContentValues();
        values.put(DatabaseHelper.COLUMN_FIRST_NAME, user.getFirstName());
        values.put(DatabaseHelper.COLUMN_LAST_NAME, user.getLastName());
        values.put(DatabaseHelper.COLUMN_EMAIL, user.getEmail());
        values.put(DatabaseHelper.COLUMN_PHONE_NUMBER, user.getPhoneNumber());
        return values;
    }

    private User cursorToUser(Cursor cursor) {
        User user = new User();
        user.setId(cursor.getLong(cursor.getColumnIndexOrThrow(DatabaseHelper.COLUMN_ID)));
        user.setFirstName(cursor.getString(cursor.getColumnIndexOrThrow(DatabaseHelper.COLUMN_FIRST_NAME)));
        user.setLastName(cursor.getString(cursor.getColumnIndexOrThrow(DatabaseHelper.COLUMN_LAST_NAME)));
        user.setEmail(cursor.getString(cursor.getColumnIndexOrThrow(DatabaseHelper.COLUMN_EMAIL)));
        user.setPhoneNumber(cursor.getString(cursor.getColumnIndexOrThrow(DatabaseHelper.COLUMN_PHONE_NUMBER)));
        user.setCreatedOn(cursor.getString(cursor.getColumnIndexOrThrow(DatabaseHelper.COLUMN_CREATED_ON)));
        return user;
    }
}
