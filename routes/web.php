<?php

use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/buttonChk', function () {
    return view('red-heading');
});

Route::get('/check', function () {
    return view('check');
});

Route::get('/empty', function () {
    return view('muji.empty');
});

Route::get('/login', function () {
    return view('login');
});