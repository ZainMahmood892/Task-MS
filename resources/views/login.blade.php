<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>
    <style>
        /* Simple CSS for login form */
        body {
            font-family: Arial, sans-serif;
            background: #f4f6f8;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .login-container {
            background: white;
            padding: 2rem 3rem;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            width: 320px;
        }
        h2 {
            margin-bottom: 1.5rem;
            text-align: center;
            color: #333;
        }
        label {
            display: block;
            margin-bottom: 0.5rem;
            color: #555;
        }
        input[type="text"], input[type="password"] {
            width: 100%;
            padding: 0.5rem;
            margin-bottom: 1rem;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
            font-size: 1rem;
        }
        button {
            width: 100%;
            background: #007bff;
            color: white;
            padding: 0.7rem;
            border: none;
            border-radius: 4px;
            font-size: 1rem;
            cursor: pointer;
            transition: background 0.3s ease;
        }
        button:hover {
            background: #0056b3;
        }
        .error {
            color: #d93025;
            margin-bottom: 1rem;
            font-size: 0.9rem;
        }
        .success {
            color: #188038;
            margin-bottom: 1rem;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h2>Login</h2>
        <div id="message"></div>
        <form id="loginForm" action="javascript:void(0);">
            <label for="username">Username</label>
            <input type="text" id="username" name="username" placeholder="Enter username" required>
            
            <label for="password">Password</label>
            <input type="password" id="password" name="password" placeholder="Enter password" required>
            
            <button type="submit">Login</button>
        </form>
    </div>

    <script>
        const loginForm = document.getElementById('loginForm');
        const messageDiv = document.getElementById('message');

        loginForm.addEventListener('submit', function(e) {
            e.preventDefault();

            const username = loginForm.username.value.trim();
            const password = loginForm.password.value.trim();

            // Simple client-side validation
            if(!username || !password) {
                showMessage('Please fill both fields.', 'error');
                return;
            }

            // Example login check (in real app send to API or backend route)
            // For demonstration, username: admin, password: password123
            if(username === 'admin' && password === 'password123') {
                showMessage('Login successful!', 'success');
                // Redirect or further action here
            } else {
                showMessage('Invalid username or password.', 'error');
            }
        });

        function showMessage(msg, type) {
            messageDiv.textContent = msg;
            messageDiv.className = type;
        }
    </script>
</body>
</html>