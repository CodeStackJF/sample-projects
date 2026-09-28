package com.example.userscrud.controllers;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.example.userscrud.R;
import com.example.userscrud.adapters.UserAdapter;
import com.example.userscrud.models.User;
import com.example.userscrud.models.UserDao;
import com.google.android.material.floatingactionbutton.FloatingActionButton;

import java.util.List;

/**
 * Pantalla principal: lista todos los usuarios.
 * Equivalente a la acción "index" de userController.js (GET /users).
 */
public class MainActivity extends AppCompatActivity implements UserAdapter.OnUserActionListener {

    public static final String EXTRA_USER_ID = "extra_user_id";

    private UserDao userDao;
    private UserAdapter adapter;
    private RecyclerView recyclerView;
    private View emptyState;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        setTitle(R.string.app_name);

        userDao = new UserDao(this);
        recyclerView = findViewById(R.id.recyclerView);
        emptyState = findViewById(R.id.emptyState);
        FloatingActionButton fabAdd = findViewById(R.id.fabAdd);

        adapter = new UserAdapter(this);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));
        recyclerView.setAdapter(adapter);

        fabAdd.setOnClickListener(v ->
                startActivity(new Intent(MainActivity.this, UserFormActivity.class)));
    }

    @Override
    protected void onResume() {
        super.onResume();
        // Recargamos cada vez que se vuelve a esta pantalla (tras crear/editar/eliminar)
        loadUsers();
    }

    private void loadUsers() {
        List<User> users = userDao.getAllUsers();
        adapter.setUsers(users);

        boolean isEmpty = users.isEmpty();
        emptyState.setVisibility(isEmpty ? View.VISIBLE : View.GONE);
        recyclerView.setVisibility(isEmpty ? View.GONE : View.VISIBLE);
    }

    @Override
    public void onView(User user) {
        Intent intent = new Intent(this, UserDetailActivity.class);
        intent.putExtra(EXTRA_USER_ID, user.getId());
        startActivity(intent);
    }

    @Override
    public void onEdit(User user) {
        Intent intent = new Intent(this, UserFormActivity.class);
        intent.putExtra(EXTRA_USER_ID, user.getId());
        startActivity(intent);
    }

    @Override
    public void onDelete(User user) {
        new AlertDialog.Builder(this)
                .setTitle("Eliminar usuario")
                .setMessage("¿Seguro que deseas eliminar a "
                        + user.getFirstName() + " " + user.getLastName() + "?")
                .setPositiveButton("Eliminar", (dialog, which) -> {
                    userDao.deleteUser(user.getId());
                    loadUsers();
                })
                .setNegativeButton("Cancelar", null)
                .show();
    }
}
