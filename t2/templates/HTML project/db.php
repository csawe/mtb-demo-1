<?php
//define PDO - tell about the database file
$pdo = new PDO('C:\Users\roymu\Documents\HTML project\db.sqlite3');
// write SQL
$statement = $pdo->query("SELECT * FROM db");
// run the SQL
$rows = $statement->fetchall(PDO::FETCH_ASSOC);
//show it on the screen
var_dump($rows);  