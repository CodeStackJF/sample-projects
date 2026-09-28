package com.ugb.countries.database;

import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class ContextDB extends SQLiteOpenHelper {
    private static final String DB_NAME = "countries.db";
    private static final int DB_VERSION = 2;

    private static ContextDB instance;

    public static synchronized ContextDB getInstance(Context context)
    {
        if(instance == null)
        {
            instance = new ContextDB(context.getApplicationContext());
        }
        return instance;
    }

    private ContextDB (Context context)
    {
        super(context, DB_NAME, null, DB_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db)
    {
        String createTable =
                "CREATE TABLE countries (" +
                        "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
                        "name TEXT NOT NULL, " +
                        "description TEXT NOT NULL, " +
                        "flag TEXT NOT NULL" +
                        ")";
        db.execSQL(createTable);

        Cursor count = db.rawQuery("SELECT 1 FROM countries", null);
        if(!count.moveToNext())
        {
            String insertRecords = "INSERT INTO countries (name, description, flag) VALUES ('El Salvador', 'El pulgarcito de América', 'el_salvador')";
            db.execSQL(insertRecords);
            insertRecords = "INSERT INTO countries (name, description, flag) VALUES ('Panamá', 'El pulgarcito de América', 'panama')";
            db.execSQL(insertRecords);
        }
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("DROP TABLE IF EXISTS countries");
        onCreate(db);
    }

}
