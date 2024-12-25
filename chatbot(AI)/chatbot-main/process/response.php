<?php
header('Content-Type: application/json');
$data = file_get_contents('responses.json');
echo $data;
?>
