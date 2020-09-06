<?php
header("Access-Control-Allow-Origin: *"); 
define('DB_USER', 'root'); // db user
define('DB_PASSWORD', ''); // db password (mention your db password here)
define('DB_DATABASE', 'footballApp'); // database name
define('DB_SERVER', 'localhost:8082'); // db server

// array for JSON response
$response = array();
 
class DB_CONNECT {

    // constructor
    function __construct() 
    {
        // connecting to database
       $this->connect();  
    }

    // destructor
    function __destruct() {
        // closing db connection
        $this->close();
    }

     function connect()
    {
    // import database connection variables
    
    
    // Connecting to mysql database
     $con = mysql_connect('localhost', 'root', '') or die(mysql_error());

     $db = mysql_select_db('footballApp', $con) or die(mysql_error()) or die(mysql_error());

        mysql_query("SET NAMES 'UTF8'");
        mysql_query("SET CHARACTER SET utf8_turkish_ci");  
       // mysql_query("SET COLLATION_CONNECTION = 'utf8_turkish_ci'");
       mysql_query("SET COLLATION_CONNECTION = 'utf8_general_ci'");
 
        return $con;
    }
    
    function close() 
    {
        mysql_close();
    }
}
 
// connecting to db
$db = new DB_CONNECT();


try {
    $conn = new PDO("mysql:host=localhost:8082;dbname=footballAppe", "root", "");
    // set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);









    $sql = "INSERT INTO epost (id, eposta, passwordd)
    VALUES ('1', 'john@example.com', 'dowe')";
    // use exec() because no results are returned
    $conn->exec($sql);
    echo "New record created successfully";
    }
catch(PDOException $e)
    {
    echo $e->getMessage();
    }

$conn = null;
?>