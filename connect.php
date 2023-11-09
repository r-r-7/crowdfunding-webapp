<?php
$conn=mysqli_connect('localhost','root','','CFWA');
if($conn){
    echo "Connection Successfull";
}else{
    die(mysqli_error("Error"+$conn));
}
?>