package com.example.userscrud.adapters;

import android.text.TextUtils;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.example.userscrud.R;
import com.example.userscrud.models.User;

import java.util.ArrayList;
import java.util.List;

/**
 * Adaptador que dibuja cada usuario como una tarjeta (item_user.xml) dentro del
 * RecyclerView de MainActivity. Es el equivalente visual al bucle
 * "users.forEach" de la vista index.ejs en el proyecto Node.
 */
public class UserAdapter extends RecyclerView.Adapter<UserAdapter.UserViewHolder> {

    /** Callback para las acciones de cada fila: ver, editar, eliminar. */
    public interface OnUserActionListener {
        void onView(User user);
        void onEdit(User user);
        void onDelete(User user);
    }

    private List<User> users = new ArrayList<>();
    private final OnUserActionListener listener;

    public UserAdapter(OnUserActionListener listener) {
        this.listener = listener;
    }

    public void setUsers(List<User> users) {
        this.users = users;
        notifyDataSetChanged();
    }

    @NonNull
    @Override
    public UserViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.item_user, parent, false);
        return new UserViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull UserViewHolder holder, int position) {
        holder.bind(users.get(position), listener);
    }

    @Override
    public int getItemCount() {
        return users.size();
    }

    static class UserViewHolder extends RecyclerView.ViewHolder {

        private final TextView textName;
        private final TextView textEmail;
        private final TextView textPhone;
        private final View btnEdit;
        private final View btnDelete;

        UserViewHolder(@NonNull View itemView) {
            super(itemView);
            textName = itemView.findViewById(R.id.textName);
            textEmail = itemView.findViewById(R.id.textEmail);
            textPhone = itemView.findViewById(R.id.textPhone);
            btnEdit = itemView.findViewById(R.id.btnEdit);
            btnDelete = itemView.findViewById(R.id.btnDelete);
        }

        void bind(User user, OnUserActionListener listener) {
            textName.setText(String.format("%s %s", user.getFirstName(), user.getLastName()));
            textEmail.setText(user.getEmail());
            textPhone.setText(TextUtils.isEmpty(user.getPhoneNumber()) ? "-" : user.getPhoneNumber());

            itemView.setOnClickListener(v -> listener.onView(user));
            btnEdit.setOnClickListener(v -> listener.onEdit(user));
            btnDelete.setOnClickListener(v -> listener.onDelete(user));
        }
    }
}
