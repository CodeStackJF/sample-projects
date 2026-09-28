package com.ugb.countries;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.AutoCompleteTextView;
import android.widget.Button;
import android.widget.EditText;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import com.ugb.countries.dao.UserDao;
import com.ugb.countries.models.Country;

public class CountryForm extends AppCompatActivity {

    EditText txtCountryName, txtCountryDescription;
    AutoCompleteTextView listFlags;
    Button btnAddCountry;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_country_form);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });

        txtCountryName = findViewById(R.id.txtCountryName);
        txtCountryDescription = findViewById(R.id.txtCountryDescription);
        listFlags = findViewById(R.id.listFlags);
        ArrayAdapter<String> flags = new ArrayAdapter<String>(this, android.R.layout.simple_dropdown_item_1line);
        flags.add("panama");
        flags.add("costa_rica");
        flags.add("guatemala");
        flags.add("honduras");
        flags.add("nicargua");
        listFlags.setAdapter(flags);
        listFlags.setThreshold(1);

        btnAddCountry = findViewById(R.id.btnAddCountry);
        UserDao userDao = new UserDao(this);

        btnAddCountry.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                userDao.Insert(new Country(
                        0,
                        txtCountryName.getText().toString(),
                        txtCountryDescription.getText().toString(),
                        listFlags.getText().toString()
                        ));
                Intent intent = new Intent(CountryForm.this, MainActivity.class);
                startActivity(intent);
            }
        });

    }
}