package com.example.userscrud.controllers;

import android.content.Intent;
import android.os.Bundle;
import android.text.TextUtils;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.example.userscrud.R;
import com.example.userscrud.models.User;
import com.example.userscrud.models.UserDao;

/**
 * Pantalla de detalle de un usuario.
 * Equivalente a la acción "show" de userController.js (GET /users/:id).
 */
public class UserDetailActivity extends AppCompatActivity {

    private UserDao userDao;
    private long userId;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_detail);
        setTitle("Detalle de usuario");

        if (getSupportActionBar() != null) {
            getSupportActionBar().setDisplayHomeAsUpEnabled(true);
        }

        userDao = new UserDao(this);
        userId = getIntent().getLongExtra(MainActivity.EXTRA_USER_ID, -1);

        TextView textName = findViewById(R.id.textDetailName);
        TextView textEmail = findViewById(R.id.textDetailEmail);
        TextView textPhone = findViewById(R.id.textDetailPhone);
        TextView textCreated = findViewById(R.id.textDetailCreated);
        Button btnEdit = findViewById(R.id.btnDetailEdit);

        User user = userDao.getUserById(userId);
        if (user == null) {
            Toast.makeText(this, "Usuario no encontrado", Toast.LENGTH_SHORT).show();
            finish();
            return;
        }

        textName.setText(String.format("%s %s", user.getFirstName(), user.getLastName()));
        textEmail.setText(user.getEmail());
        textPhone.setText(TextUtils.isEmpty(user.getPhoneNumber()) ? "-" : user.getPhoneNumber());
        textCreated.setText(getString(R.string.created_on) + ": " + user.getCreatedOn());

        btnEdit.setOnClickListener(v -> {
            Intent intent = new Intent(UserDetailActivity.this, UserFormActivity.class);
            intent.putExtra(MainActivity.EXTRA_USER_ID, userId);
            startActivity(intent);
        });
    }

    @Override
    public boolean onSupportNavigateUp() {
        onBackPressed();
        return true;
    }
}
