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

Route::get('/authController', function () {
    return view('app.Http.Controllers.AuthController');
});

Route::get('/database.migrations.0003_01_01_000000_create_products_table', function () {
    return view('database.migrations.0003_01_01_000000_create_products_table');
});

Route::get('/header', function () {
    return view('header');
});