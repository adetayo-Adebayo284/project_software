<?php
	define("DB_HOST", "localhost");
	define("DB_NAME", "bookstoredatabase");
	define("DB_USER", "root");
	define("DB_PASS", "");

	try 
	{

		// Connection to database
		$connection_database = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
		
	}
	catch(Exception $error) 
	{
		header("location: book/Bookstore-Management-System-PHP-MySQL-Project-main/500.php");
	}
?>