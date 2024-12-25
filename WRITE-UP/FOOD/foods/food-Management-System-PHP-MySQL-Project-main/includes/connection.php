<?php
	define("DB_HOST", "localhost");
	define("DB_NAME", "food");
	define("DB_USER", "root");
	define("DB_PASS", "");

	try 
	{

		// Connection to database   bookstoredatabase
		$connection_database = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
		
	}
	catch(Exception $error) 
	{
		header("location: foods/food-Management-System-PHP-MySQL-Project-main/500.php");
	}
?>