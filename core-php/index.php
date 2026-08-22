<?php
session_start();
if (isset($_SESSION['user_email'])) {
    header('Location: dashboard.php');
    exit();
}

// Check for error messages
$error = '';
if (isset($_SESSION['login_error'])) {
    $error = $_SESSION['login_error'];
    unset($_SESSION['login_error']);
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Form</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f7f7f7; }
        .container { max-width: 400px; margin: 80px auto; background: #fff; padding: 30px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        h2 { text-align: center; margin-bottom: 20px; }
        label { display: block; margin-bottom: 6px; font-weight: bold; }
        input[type="email"], input[type="password"] {
            width: 100%; padding: 10px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 4px;
            box-sizing: border-box;
        }
        button {
            width: 100%; padding: 10px; background-color: #28a745; color: white; border: none;
            border-radius: 4px; font-size: 16px; cursor: pointer;
        }
        button:hover { background-color: #218838; }
        .error { color: #cc0000; margin-bottom: 15px; text-align: center; }
    </style>
</head>
<body>
<div class="container">
    <h2>Login</h2>
    <?php if ($error): ?>
        <div class="error" role="alert"><?php echo htmlspecialchars($error, ENT_QUOTES, 'UTF-8'); ?></div>
    <?php endif; ?>
    <form action="login.php" method="post" autocomplete="off" novalidate>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" placeholder="Enter your email" required autofocus>

        <label for="password">Password:</label>
        <input type="password" id="password" name="password" placeholder="Enter your password" required minlength="6">

        <button type="submit">Login</button>
    </form>
</div>
</body>
</html>
