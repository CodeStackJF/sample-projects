<?php

namespace App\Http\Controllers;

use App\Models\Chirp;
use Illuminate\Http\Request;

class ChirpController extends Controller
{
    /* public function index()
    {
        $chirps = [
            [
                'author' => 'Jane Doe',
                'message' => 'Just deployed my first Laravel app! 🚀',
                'time' => '5 minutes ago'
            ],
            [
                'author' => 'John Smith',
                'message' => 'Laravel makes web development fun again!',
                'time' => '1 hour ago'
            ],
            [
                'author' => 'Alice Johnson',
                'message' => 'Working on something cool with Chirper...',
                'time' => '3 hours ago'
            ]
        ];

        return view('home.home', ['chirps' => $chirps]);
    } */

        public function index()
        {
            $chirps = Chirp::with('user')->latest()->take(50)->get();
            return view('home', ['chirps' => $chirps]);
        }
}
