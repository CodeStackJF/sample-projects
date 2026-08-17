<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class UserController extends Controller
{
    public function index()
    {
        $users = [
            [
                'id'=>1,
                'name'=>'jose',
                'email' => 'jfuentes@ugb.edu.sv'
            ],
            [
                'id'=>2,
                'name'=>'juan',
                'email' => 'juan@ugb.edu.sv'
            ]
        ];
        return view('users.index', ['users' => $users]);
    }
}
