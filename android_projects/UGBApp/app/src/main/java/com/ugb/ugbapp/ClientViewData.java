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

import com.ugb.ugbapp.models.Client;

public class ClientViewData extends AppCompatActivity {

    Button btnReturnToClientManager;
    TextView tvFirstName, tvLastName;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_client_view_data);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });

        tvFirstName = findViewById(R.id.tvFirstNameReceived);
        tvLastName = findViewById(R.id.tvLastNameReceived);

        Intent intentClientViewData = getIntent();
        String firstName = intentClientViewData.getStringExtra("firstName");
        String lastName = intentClientViewData.getStringExtra("lastName");
        /*tvFirstName.setText(firstName);
        tvLastName.setText(lastName);*/
        Client client = (Client)intentClientViewData.getSerializableExtra("client");
        if(client != null){
            tvFirstName.setText(client.getFirstName());
            tvLastName.setText(client.getLastName());
        }

        btnReturnToClientManager = findViewById(R.id.btnReturnToClientManager);
        btnReturnToClientManager.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(ClientViewData.this, ClientManager.class);
                startActivity(intent);
            }
        });
    }
}