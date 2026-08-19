<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>App Header</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <!-- Tailwind CSS CDN for quick prototyping -->
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
    <header class="bg-gradient-to-r from-blue-600 to-indigo-700 shadow-md">
        <div class="container mx-auto flex items-center justify-between py-4 px-6">
            <a href="{{ url('/') }}" class="flex items-center space-x-3">
                <img src="{{ asset('images/logo.svg') }}" alt="App Logo" class="h-10 w-10">
                <span class="text-white text-xl font-bold tracking-wide">MyApp</span>
            </a>
            <nav>
                <ul class="flex space-x-6 text-white font-semibold">
                    <li>
                        <a href="{{ url('/') }}" class="hover:text-yellow-300 transition duration-300">Home</a>
                    </li>
                    <li>
                        <a href="{{ url('/about') }}" class="hover:text-yellow-300 transition duration-300">About</a>
                    </li>
                    <li>
                        <a href="{{ url('/services') }}" class="hover:text-yellow-300 transition duration-300">Services</a>
                    </li>
                    <li>
                        <a href="{{ url('/contact') }}" class="hover:text-yellow-300 transition duration-300">Contact</a>
                    </li>
                    @auth
                        <li>
                            <a href="{{ url('/dashboard') }}" class="hover:text-yellow-300 transition duration-300">Dashboard</a>
                        </li>
                        <li>
                            <form method="POST" action="{{ route('logout') }}">
                                @csrf
                                <button type="submit" class="hover:text-yellow-300 transition duration-300">Logout</button>
                            </form>
                        </li>
                    @else
                        <li>
                            <a href="{{ route('login') }}" class="hover:text-yellow-300 transition duration-300">Login</a>
                        </li>
                        <li>
                            <a href="{{ route('register') }}" class="hover:text-yellow-300 transition duration-300">Register</a>
                        </li>
                    @endauth
                </ul>
            </nav>
        </div>
    </header>
</body>
</html>