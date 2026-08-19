<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Header Example</title>
    <style>
        /* Basic reset */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        /* Header styling */
        header {
            background-color: #1E40AF; /* blue-800 */
            color: white;
            padding: 20px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        /* Logo styling */
        .logo {
            font-size: 1.8rem;
            font-weight: 700;
            letter-spacing: 2px;
            cursor: pointer;
            user-select: none;
        }
        /* Navigation menu */
        nav ul {
            list-style: none;
            display: flex;
            gap: 30px;
        }
        nav ul li a {
            color: white;
            text-decoration: none;
            font-weight: 600;
            font-size: 1rem;
            transition: color 0.3s ease;
        }
        nav ul li a:hover {
            color: #93C5FD; /* light blue */
        }
        /* Responsive for smaller screens */
        @media (max-width: 600px) {
            header {
                flex-direction: column;
                padding: 15px 20px;
            }
            nav ul {
                flex-direction: column;
                gap: 15px;
                margin-top: 15px;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="logo">MyWebsite</div>
        <nav>
            <ul>
                <li><a href="{{ url('/') }}">Home</a></li>
                <li><a href="{{ url('/about') }}">About</a></li>
                <li><a href="{{ url('/services') }}">Services</a></li>
                <li><a href="{{ url('/contact') }}">Contact</a></li>
            </ul>
        </nav>
    </header>
</body>
</html>