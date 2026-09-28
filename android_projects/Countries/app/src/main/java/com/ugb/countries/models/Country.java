package com.ugb.countries.models;

import java.io.Serializable;

public class Country implements Serializable {
    private int id;
    private String name;
    private String description;
    private String flag;

    public Country(int id, String name, String description, String flag)
    {
        this.id = id;
        this.name = name;
        this.description = description;
        this.flag = flag;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getFlag() {
        return flag;
    }

    public void setFlag(String flag) {
        this.flag = flag;
    }
}
