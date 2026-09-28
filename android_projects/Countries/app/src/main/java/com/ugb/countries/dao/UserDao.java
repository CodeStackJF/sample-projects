package com.ugb.countries.dao;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.util.Log;

import com.ugb.countries.database.ContextDB;
import com.ugb.countries.models.Country;

import java.util.ArrayList;
import java.util.List;

public class UserDao {
    private final ContextDB ctx;

    public UserDao(Context context)
    {
        this.ctx = ContextDB.getInstance(context);
        SQLiteDatabase db = ctx.getWritableDatabase();
        Log.d("DATABASE", "Ruta: " + db.getPath());
    }

    public List<Country> getAll()
    {
        List<Country> countries = new ArrayList<>();
        SQLiteDatabase db = ctx.getReadableDatabase();
        Cursor cursor = db.rawQuery("SELECT * FROM countries", null);
        if(cursor != null)
        {
            while(cursor.moveToNext())
            {
                countries.add(mapCursorToCountry(cursor));
            }
            cursor.close();
        }
        return countries;
    }

    public boolean Delete(int id)
    {
        SQLiteDatabase db = ctx.getWritableDatabase();
        int rows = db.delete(
                "countries",
                "id = ?",
                new String[]{String.valueOf(id)}
        );
        return rows > 0;
    }

    public void Insert(Country country)
    {
        SQLiteDatabase db = ctx.getReadableDatabase();
        ContentValues values = buildContentValues(country);
        db.insertOrThrow("countries", null, values);
    }

    private ContentValues buildContentValues(Country country) {
        ContentValues values = new ContentValues();
        values.put("name", country.getName());
        values.put("description", country.getDescription());
        values.put("flag", country.getFlag());
        return values;
    }

    private Country mapCursorToCountry(Cursor cursor)
    {
        return new Country(
                cursor.getInt(cursor.getColumnIndexOrThrow("id")),
                cursor.getString(cursor.getColumnIndexOrThrow("name")),
                cursor.getString(cursor.getColumnIndexOrThrow("description")),
                cursor.getString(cursor.getColumnIndexOrThrow("flag"))
        );
    }

}
