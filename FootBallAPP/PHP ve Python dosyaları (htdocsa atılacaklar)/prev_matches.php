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

$team = $_GET['team'];

// connecting to db
$db = new DB_CONNECT();


// get all ülkeler from ulkeler table
$result = mysql_query("SELECT * FROM `$team`") or die(mysql_error());

// check for empty result
if (mysql_num_rows($result) > 0) {
    // looping through all results
    // ulkeler node
    //$response["home_stats"] = array();
 
    while ($row = mysql_fetch_array($result)) {
        // temp user array
        $match = array();
        $match["home_team"] = $row["home_team"];
        $match["away_team"] = $row["away_team"];
        $match["half_score_0"] = $row["half_score_0"];
        $match["half_score_1"] = $row["half_score_1"];
        $match["score_0"] = $row["score_0"];
        $match["score_1"] = $row["score_1"];
 
//         // push single musteri into final response array
//         //array_push($response["home_stats"], $team);
        array_push($response, $match);
    }
//     // success
//     //$response["success"] = 1;
 
//     // echoing JSON response
    echo json_encode($response);
//    //echo utf8_encode($response);
} else {
    // no musterilerim found
    $response["success"] = 0;
    $response["message"] = "No country found";
 
    // echo no users JSON
    echo json_encode($response);
    // echo utf8_encode($response);
}
?>