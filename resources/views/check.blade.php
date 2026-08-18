<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Login Form</title>
    <style>
        /* Reset some basic elements */
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        body, html {
            height: 100%;
            background: #f0f2f5;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .login-container {
            background: #fff;
            padding: 40px 35px;
            width: 350px;
            border-radius: 8px;
            box-shadow: 0 12px 24px rgba(0,0,0,0.15);
            transition: box-shadow 0.3s ease;
        }
        .login-container:hover {
            box-shadow: 0 18px 36px rgba(0,0,0,0.2);
        }
        .login-container h2 {
            text-align: center;
            margin-bottom: 30px;
            color: #333;
            letter-spacing: 1px;
        }
        form {
            display: flex;
            flex-direction: column;
        }
        label {
            margin-bottom: 8px;
            font-weight: 600;
            color: #555;
        }
        input[type="email"],
        input[type="password"] {
            padding: 12px 15px;
            margin-bottom: 20px;
            border: 1.8px solid #ddd;
            border-radius: 5px;
            font-size: 16px;
            transition: border-color 0.3s ease;
        }
        input[type="email"]:focus,
        input[type="password"]:focus {
            border-color: #4a90e2;
            outline: none;
            box-shadow: 0 0 8px rgba(74,144,226,0.3);
        }
        button {
            padding: 12px 15px;
            background-color: #4a90e2;
            border: none;
            border-radius: 5px;
            color: white;
            font-size: 17px;
            font-weight: 600;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #357ab8;
        }
        /* Responsive */
        @media (max-width: 400px) {
            .login-container {
                width: 90%;
                padding: 30px 20px;
            }
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h2>Login</h2>
        <form method="POST" action="#">
            @csrf
            <label for="email">Email</label>
            <input type="email" id="email" name="email" placeholder="you@example.com" required autocomplete="email" />
            
            <label for="password">Password</label>
            <input type="password" id="password" name="password" placeholder="Enter your password" required autocomplete="current-password" />
            
            <button type="submit">Login</button>
        </form>
    </div>
</body>
</html>