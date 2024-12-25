<?php
	session_start();

	session_destroy();

	header("location: ../../Bookstore-Management-System-PHP-MySQL-Project-main/");
	
	exit();
?>