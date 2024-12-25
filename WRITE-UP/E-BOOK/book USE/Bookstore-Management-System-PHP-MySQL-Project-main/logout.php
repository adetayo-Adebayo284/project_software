<?php
    // Start or resume the PHP session
    session_start();

    // Destroy the current session, effectively logging the user out
    session_destroy();

    // Redirect the user to the "index.php" page
    header("location: /book/Bookstore-Management-System-PHP-MySQL-Project-main/");

    exit();
?>