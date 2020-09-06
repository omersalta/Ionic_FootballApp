<?php

$command = escapeshellcmd('python ./web_crawling.py');
$output = shell_exec($command);

 ?>