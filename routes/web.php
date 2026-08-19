<?php

use Illuminate\Support\Facades\Route;

// Other routes here...

// Removed the route: Route::get('/css.header', function () {
//     return view('css.header');
// });

// Add your other routes below as needed.

Route::get('/css/header', function () {
    return view('css.header');
});

Route::get('/header', function () {
    return view('header');
});

Route::get('/footer', function () {
    return view('footer');
});