<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Header</title>
    <style>
        /* Assuming existing header styles here */
        header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 10px 20px;
            background-color: #f8f9fa;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .logo {
            font-size: 1.5rem;
            font-weight: bold;
            color: #333;
        }
        nav {
            display: flex;
            gap: 15px;
            align-items: center;
        }
        nav a {
            text-decoration: none;
            color: #333;
            font-weight: 500;
            padding: 6px 12px;
            border-radius: 4px;
            transition: background-color 0.3s ease;
        }
        nav a:hover {
            background-color: #e2e6ea;
        }
        /* New button style */
        .header-button {
            background-color: black;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 4px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .header-button:hover,
        .header-button:focus {
            background-color: #222;
            outline: none;
        }
        /* Responsive adjustments */
        @media (max-width: 600px) {
            header {
                flex-direction: column;
                align-items: flex-start;
            }
            nav {
                width: 100%;
                justify-content: flex-start;
                flex-wrap: wrap;
                gap: 10px;
                margin-top: 10px;
            }
            .header-button {
                width: 100%;
                text-align: center;
            }
        }
    </style>
</head>
<body>
<header>
    <div class="logo">MySite</div>
    <nav>
        <a href="/home">Home</a>
        <a href="/about">About</a>
        <a href="/services">Services</a>
        <!-- New button added here inside nav for proper placement -->
        <button type="button" class="header-button">New Button</button>
    </nav>
</header>
</body>
</html>