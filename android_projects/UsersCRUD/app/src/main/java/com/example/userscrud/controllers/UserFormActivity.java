package com.example.userscrud.controllers;

import android.os.Bundle;
import android.text.TextUtils;
import android.util.Patterns;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.example.userscrud.R;
import com.example.userscrud.models.User;
import com.example.userscrud.models.UserDao;

/**
 * Formulario de creación y edición de usuario.
 * Si llega EXTRA_USER_ID en el Intent, actúa como "edit" (PUT);
 * si no, actúa como "new"/"create" (POST). Es el equivalente a
 * newForm/create/editForm/update de userController.js.
 */
public class UserFormActivity extends AppCompatActivity {

    private UserDao userDao;
    private EditText editFirstName;
    private EditText editLastName;
    private EditText editEmail;
    private EditText editPhone;

    private long userId = -1;
    private User currentUser;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_form);

        userDao = new UserDao(this);
        editFirstName = findViewById(R.id.editFirstName);
        editLastName = findViewById(R.id.editLastName);
        editEmail = findViewById(R.id.editEmail);
        editPhone = findViewById(R.id.editPhone);
        Button btnSave = findViewById(R.id.btnSave);

        userId = getIntent().getLongExtra(MainActivity.EXTRA_USER_ID, -1);

        if (userId != -1) {
            setTitle("Editar usuario");
            currentUser = userDao.getUserById(userId);
            if (currentUser != null) {
                editFirstName.setText(currentUser.getFirstName());
                editLastName.setText(currentUser.getLastName());
                editEmail.setText(currentUser.getEmail());
                editPhone.setText(currentUser.getPhoneNumber());
            }
        } else {
            setTitle("Nuevo usuario");
        }

        if (getSupportActionBar() != null) {
            getSupportActionBar().setDisplayHomeAsUpEnabled(true);
        }

        btnSave.setOnClickListener(v -> saveUser());
    }

    @Override
    public boolean onSupportNavigateUp() {
        onBackPressed();
        return true;
    }

    private void saveUser() {
        String firstName = editFirstName.getText().toString().trim();
        String lastName = editLastName.getText().toString().trim();
        String email = editEmail.getText().toString().trim();
        String phone = editPhone.getText().toString().trim();

        // Validaciones básicas, equivalentes a las reglas de express-validator
        if (TextUtils.isEmpty(firstName)) {
            editFirstName.setError("El nombre es obligatorio");
            editFirstName.requestFocus();
            return;
        }
        if (TextUtils.isEmpty(lastName)) {
            editLastName.setError("El apellido es obligatorio");
            editLastName.requestFocus();
            return;
        }
        if (TextUtils.isEmpty(email) || !Patterns.EMAIL_ADDRESS.matcher(email).matches()) {
            editEmail.setError("Ingresa un email válido");
            editEmail.requestFocus();
            return;
        }

        User user = (userId != -1 && currentUser != null) ? currentUser : new User();
        user.setFirstName(firstName);
        user.setLastName(lastName);
        user.setEmail(email);
        user.setPhoneNumber(phone);

        UserDao.Result result = (userId != -1)
                ? userDao.updateUser(user)
                : userDao.insertUser(user);

        if (result.success) {
            Toast.makeText(this,
                    userId != -1 ? "Usuario actualizado correctamente" : "Usuario creado correctamente",
                    Toast.LENGTH_SHORT).show();
            finish();
        } else {
            // Ej. violación de la restricción UNIQUE sobre email
            editEmail.setError(result.errorMessage);
            editEmail.requestFocus();
            Toast.makeText(this, result.errorMessage, Toast.LENGTH_SHORT).show();
        }
    }
}
