# Core PHP Login Form Application

This is a simple core PHP-based login form project demonstrating user authentication with session handling.

## Features

- Login form with email and password inputs.
- Basic validation and sanitization of user input.
- Password verification with secure hashed passwords.
- Session management with session fixation protection.
- Protected dashboard page accessible only to logged-in users.
- Simple logout functionality that destroys the user session.
- Simulated user database with hashed passwords stored in `users.php`.
- `.htaccess` file for basic access control and security hardening.

## Files Structure

```
core-php/
│
├── index.php       # Login page form
├── login.php       # Handles login logic and session set
├── logout.php      # Destroys session and logs out user
├── dashboard.php   # Protected page
├── users.php       # Simulated user store with hashed passwords
├── .htaccess       # Apache security config
└── README.md       # This file
```

## Setup Instructions

1. **Requirements:**
   - PHP 7.3 or higher (recommended PHP 8+)
   - Apache or any webserver capable of running PHP

2. Copy the `core-php` folder to your web server directory.

3. Ensure PHP sessions work and write to a temp folder correctly.

4. If using Apache, `.htaccess` is included to:
   - Deny direct access to `users.php` (for security).
   - Increase security with some HTTP headers.
   - Disable directory listing.

5. Access the application via your browser:
   - `http://your-server/core-php/index.php`

## Usage

- Use one of the pre-defined user credentials from `users.php` to login:

  | Email                | Password     |
  |----------------------|--------------|
  | user1@example.com    | Password123  |
  | admin@example.com    | AdminPass456 |
  | test.user@example.com| Test@789     |

- After logging in, you will be redirected to `dashboard.php`.
- Use the "Logout" button to end your session.

## Security Notes

- Passwords are hashed with PHP's `password_hash()` using bcrypt.
- Sessions are protected by regenerating session IDs on login.
- Inputs are validated and sanitized.
- Direct access to `users.php` is blocked via `.htaccess`.

## Extending

- This project uses a simple in-memory simulated user database.
  You can extend it by connecting to a real database (MySQL/PostgreSQL) and
  replacing `users.php` logic with actual DB queries with prepared statements.

- Additional security measures include rate limiting, HTTPS, CSRF protection,
  and secure cookie flags that should be added in a production environment.

## License

This is a simple example provided for educational purposes.
