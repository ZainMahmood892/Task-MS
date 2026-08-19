<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sidebar</title>
    <style>
        /* Sidebar container */
        .sidebar {
            height: 100vh;
            width: 250px;
            position: fixed;
            top: 0;
            left: 0;
            background-color: #2c3e50;
            padding-top: 20px;
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
        }

        /* Sidebar links */
        .sidebar a {
            padding: 15px 25px;
            text-decoration: none;
            font-size: 18px;
            color: #ecf0f1;
            display: block;
            transition: background-color 0.3s, color 0.3s;
        }

        /* Hover effect */
        .sidebar a:hover {
            background-color: #34495e;
            color: #1abc9c;
        }

        /* Active/current link */
        .sidebar a.active {
            background-color: #1abc9c;
            color: white;
        }

        /* Content area */
        .content {
            margin-left: 250px;
            padding: 20px;
            font-family: Arial, sans-serif;
        }

        /* Sidebar header */
        .sidebar-header {
            font-size: 24px;
            font-weight: bold;
            color: #ecf0f1;
            padding: 0 25px 20px;
            border-bottom: 1px solid #34495e;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="sidebar">
        <div class="sidebar-header">My Sidebar</div>
        <a href="#" class="active">Dashboard</a>
        <a href="#">Profile</a>
        <a href="#">Messages</a>
        <a href="#">Settings</a>
        <a href="#">Logout</a>
    </div>

    <div class="content">
        <h1>Welcome to the Sidebar Page</h1>
        <p>This is an example page with a fixed sidebar navigation using HTML and CSS.</p>
    </div>
</body>
</html>