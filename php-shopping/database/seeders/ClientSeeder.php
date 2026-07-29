<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class ClientSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        User::create([
            'first_name' => 'Priscila',
            'last_name' => 'Martínez',
            'document' => '04255101-3',
            'email' => 'pmartinez@ugb.edu.sv'
        ]);
    }
}
