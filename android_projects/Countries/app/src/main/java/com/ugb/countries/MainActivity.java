package com.ugb.countries;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ListAdapter;
import android.widget.ListView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.ugb.countries.adapters.CountryAdapter;
import com.ugb.countries.dao.UserDao;
import com.ugb.countries.models.Country;

import java.util.List;

public class MainActivity extends AppCompatActivity {

    ListView lvCountries;
    UserDao userDao;
    //ListAdapter laCountry;
    CountryAdapter countryAdapter;
    FloatingActionButton btnCallAddCountry;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });

        lvCountries = findViewById(R.id.lvCountries);
        userDao = new UserDao(this);
        List<Country> countries = userDao.getAll();
        countryAdapter = new CountryAdapter(MainActivity.this, R.layout.activity_country_component, countries);
        lvCountries.setAdapter(countryAdapter);

        btnCallAddCountry = findViewById(R.id.btnCallAddCountry);
        btnCallAddCountry.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this, CountryForm.class);
                startActivity(intent);
            }
        });
    }
}