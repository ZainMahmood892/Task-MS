<?php
session_start();
require_once 'users.php';

// Validate POST method
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405); // Method Not Allowed
    exit('Invalid request method.');
}

// Basic input validation
$email = isset($_POST['email']) ? trim($_POST['email']) : '';
$password = isset($_POST['password']) ? $_POST['password'] : '';

// Validate inputs
if (empty($email) || empty($password)) {
    $_SESSION['login_error'] = 'Please enter both email and password.';
    header('Location: index.php');
    exit();
}

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    $_SESSION['login_error'] = 'Invalid email format.';
    header('Location: index.php');
    exit();
}

// Check if user exists
if (!isset($users[$email])) {
    $_SESSION['login_error'] = 'Incorrect email or password.';
    header('Location: index.php');
    exit();
}

// Verify password
$hashedPassword = $users[$email];
if (!password_verify($password, $hashedPassword)) {
    $_SESSION['login_error'] = 'Incorrect email or password.';
    header('Location: index.php');
    exit();
}

// Credentials valid - regenerate session id to prevent session fixation
session_regenerate_id(true);

// Set session variable
$_SESSION['user_email'] = $email;

// Redirect to dashboard
header('Location: dashboard.php');
exit();
