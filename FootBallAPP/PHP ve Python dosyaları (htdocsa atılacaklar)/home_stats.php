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
 
$HOME = $_GET['HOME'];
$AWAy = $_GET['AWAY'];


$AWAY = addslashes($AWAy);    
// connecting to db

$db = new DB_CONNECT();


// get all ülkeler from ulkeler table
$result = mysql_query("SELECT AVG($HOME.half_score_0) ,  STDDEV_SAMP($HOME.half_score_0), AVG($HOME.score_0 - $HOME.half_score_0), STDDEV_SAMP($HOME.score_0 - $HOME.half_score_0),
AVG(${'AWAY'}.half_score_1) ,  STDDEV_SAMP(${'AWAY'}.half_score_1) ,      AVG(${'AWAY'}.score_1 - ${'AWAY'}.half_score_1), STDDEV_SAMP(${'AWAY'}.score_1 - ${'AWAY'}.half_score_1) FROM $HOME,${'AWAY'} WHERE $HOME.home_team='$HOME'and ${'AWAY'}.away_team='${'AWAY'}'") or die(mysql_error());
          	

// check for empty result
if (mysql_num_rows($result) > 0) {
    // looping through all results
    // ulkeler node
    //$response["home_stats"] = array();
 
    while ($row = mysql_fetch_array($result)) {
        // temp user array
        $team = array();
        $team["homeA0"] = $row["AVG($HOME.half_score_0)"];
        $team["homeS0"] = $row["STDDEV_SAMP($HOME.half_score_0)"];
        $team["homeA1"] = $row["AVG($HOME.score_0 - $HOME.half_score_0)"];
        $team["homeS1"] = $row["STDDEV_SAMP($HOME.score_0 - $HOME.half_score_0)"];
        $team["awayA0"] = $row["AVG($AWAY.half_score_1)"];
        $team["awayS0"] = $row["STDDEV_SAMP($AWAY.half_score_1)"];
        $team["awayA1"] = $row["AVG($AWAY.score_1 - $AWAY.half_score_1)"];
        $team["awayS1"] = $row["STDDEV_SAMP($AWAY.score_1 - $AWAY.half_score_1)"];
        
 
        // push single musteri into final response array
        //array_push($response["home_stats"], $team);
        array_push($response, $team);
    }
    // success
    //$response["success"] = 1;
 
    // echoing JSON response
    echo json_encode($response);
   //echo utf8_encode($response);
} else {
    // no musterilerim found
    $response["success"] = 0;
    $response["message"] = "No country found";
 
    // echo no users JSON
    echo json_encode($response);
    // echo utf8_encode($response);
}
?>