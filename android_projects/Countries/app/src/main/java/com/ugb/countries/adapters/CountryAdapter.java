package com.ugb.countries.adapters;

import android.content.Context;
import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.ugb.countries.CountryForm;
import com.ugb.countries.MainActivity;
import com.ugb.countries.dao.UserDao;
import com.ugb.countries.models.Country;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import com.ugb.countries.R;
import java.util.List;

public class CountryAdapter extends ArrayAdapter<Country> {
    private List<Country> lCountries;
    private Context mCountryContext;
    private int resourceLayout;

    public CountryAdapter(@NonNull Context context, int resource, List<Country> lCountries)
    {
        super(context, resource, lCountries);
        this.lCountries = lCountries;
        this.mCountryContext = context;
        this.resourceLayout = resource;
    }

    @NonNull
    @Override
    public View getView(int position, @Nullable View convertView, @NonNull ViewGroup parent)
    {
        View view = convertView;
        if(view == null)
        {
            view = LayoutInflater.from(mCountryContext).inflate(R.layout.activity_country_component, parent, false);
        }

        Country country = lCountries.get(position);
        TextView tvCountryName = (TextView) view.findViewById(R.id.tvCountryName);
        TextView tvCountryDescription = (TextView) view.findViewById(R.id.tvCountryDescription);
        ImageView imvFlag = (ImageView) view.findViewById(R.id.imvFlag);
        Button btnEdit = (Button)view.findViewById(R.id.btnEditCountry);
        Button btnDelete = (Button)view.findViewById(R.id.btnDeleteCountry);

        tvCountryName.setText(country.getName());
        tvCountryDescription.setText(country.getDescription());
        int imageId = mCountryContext.getResources().getIdentifier(country.getFlag(), "drawable", getContext().getPackageName());
        imvFlag.setImageResource(imageId);

        UserDao userDao = new UserDao(mCountryContext);

        btnDelete.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(mCountryContext, "" + country.getId(), Toast.LENGTH_SHORT).show();
                userDao.Delete(country.getId());
                remove(country);
                notifyDataSetChanged();
            }
        });

        btnEdit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(mCountryContext, CountryForm.class);
                intent.putExtra("country", country);
                mCountryContext.startActivity(intent);
            }
        });

        return view;
    }
}
