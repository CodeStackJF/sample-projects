package com.ugb.ugbapp;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity {

    Button btnExit, btnCallClientActivity, btnCounter, btnCallCountriesActivity;
    TextView tvCounter;
    int counter = 0;

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

        btnExit = findViewById(R.id.btnExit);
        btnCallClientActivity = findViewById(R.id.btnCallClientActivity);
        btnCounter = findViewById(R.id.btnCounter);
        tvCounter = findViewById(R.id.tvCounter);
        btnCallCountriesActivity = findViewById(R.id.btnCallCountriesActivity);

        btnExit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish();
            }
        });

        btnCounter.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                counter++;
                tvCounter.setText(""+counter);
            }
        });

        btnCallClientActivity.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intentClientManager = new Intent(MainActivity.this, ClientManager.class);
                startActivity(intentClientManager);
            }
        });

        btnCallCountriesActivity.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this, Countries.class);
                startActivity(intent);
            }
        });
    }
}