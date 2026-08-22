<?php
session_start();
if (!isset($_SESSION['user_email'])) {
    // Not logged in
    header('Location: index.php');
    exit();
}

$user_email = $_SESSION['user_email'];
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #edf2f7; margin: 0; padding: 0; }
        .container { max-width: 600px; margin: 100px auto; background: #fff; border-radius: 8px; padding: 40px; box-shadow: 0 0 15px rgba(0,0,0,0.1); text-align: center; }
        h1 { color: #333; }
        p { font-size: 18px; color: #555; margin-bottom: 30px; }
        a.logout {
            display: inline-block;
            padding: 10px 20px;
            background-color: #dc3545;
            color: #fff;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
        }
        a.logout:hover {
            background-color: #c82333;
        }
    </style>
</head>
<body>
<div class="container">
    <h1>Welcome, <?php echo htmlspecialchars($user_email, ENT_QUOTES, 'UTF-8'); ?>!</h1>
    <p>You have successfully logged in to the protected dashboard page.</p>
    <a href="logout.php" class="logout" role="button">Logout</a>
</div>
</body>
</html>
