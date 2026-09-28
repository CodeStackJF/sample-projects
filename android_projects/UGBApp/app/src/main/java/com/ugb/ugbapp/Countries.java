package com.ugb.ugbapp;

import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import java.util.ArrayList;

public class Countries extends AppCompatActivity {

    ListView lvCountries;
    Button btnAddCountry;
    TextView txtCountry;
    ArrayList<String> countries = new ArrayList<String>();
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_countries);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });

        lvCountries = findViewById(R.id.lvCountries);
        ArrayAdapter<String> adapterCountries = new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, countries);
        lvCountries.setAdapter(adapterCountries);
        txtCountry = findViewById(R.id.txtCountryName);

        countries.add("El Salvador");
        countries.add("Nicaragua");
        countries.add("Honduras");
        countries.add("Panamá");

        btnAddCountry = findViewById(R.id.btnAddCountry);
        btnAddCountry.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String country = txtCountry.getText().toString();
                countries.add(country);
                adapterCountries.notifyDataSetChanged();
            }
        });

        lvCountries.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                String country = countries.get(position);
                Toast.makeText(Countries.this, "Clicked on " + country, Toast.LENGTH_SHORT).show();
            }
        });
    }
}