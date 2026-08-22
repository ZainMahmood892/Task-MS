<?php
// This file simulates a user database with emails as keys and hashed passwords as values
// Passwords are hashed with password_hash() with PASSWORD_DEFAULT (bcrypt)

$users = [
    // email => hashed_password
    'user1@example.com' => '$2y$10$LyLTx7DymK4mP9zBvEHhHu67j5pExdh9pYTcMkR77XcpLcKwBre2W', // password: Password123
    'admin@example.com' => '$2y$10$8WXp/zKxd.g0ebfujQBELO09IqEtk0i3Z/FnLjMUVUJvKcVc1RMas',  // password: AdminPass456
    'test.user@example.com' => '$2y$10$woAO/95oxYdxqJxqZ4Ey4OFUn7GvFMrP3ZnR2I8DLQfZt43EIyhHK' // password: Test@789
];

// You can regenerate hashes with the following code:
// echo password_hash('Password123', PASSWORD_DEFAULT);
// echo password_hash('AdminPass456', PASSWORD_DEFAULT);
// echo password_hash('Test@789', PASSWORD_DEFAULT);
?>
