package com.ugb.ugbapp;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import com.ugb.ugbapp.models.Client;

public class ClientManager extends AppCompatActivity {

    Button btnBackToHome, btnSaveClient;
    TextView txtFirstName, txtLastName, txtEmail;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_client_manager);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });

        btnBackToHome = findViewById(R.id.btnReturnHome);
        btnBackToHome.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intentHome = new Intent(ClientManager.this, MainActivity.class);
                startActivity(intentHome);
            }
        });

        txtFirstName = findViewById(R.id.txtFirstName);
        txtLastName = findViewById(R.id.txtLastName);
        txtEmail = findViewById(R.id.txtEmail);
        btnSaveClient = findViewById(R.id.btnSaveClient);

        btnSaveClient.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String firstName = txtFirstName.getText().toString();
                String lastName = txtLastName.getText().toString();
                String email = txtEmail.getText().toString();
                Intent intentClientViewData = new Intent(ClientManager.this, ClientViewData.class);
                intentClientViewData.putExtra("firstName", firstName);
                intentClientViewData.putExtra("lastName", lastName);
                intentClientViewData.putExtra("email", email);

                Client client = new Client(firstName, lastName, email);
                intentClientViewData.putExtra("client", client);

                startActivity(intentClientViewData);

                //Toast.makeText(ClientManager.this, firstName + "|" + lastName + "|" + email + "", Toast.LENGTH_SHORT).show();

            }
        });


    }
}