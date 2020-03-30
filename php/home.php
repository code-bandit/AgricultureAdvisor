<?php
    /*
        Home Page
    */

    session_start();
    require_once "config.php";
?>

<!DOCTYPE html>
<html lan="en">

<head>
    
    <title>Home</title> 
    <link rel="stylesheet" type="text/css" href="css/home.css">

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script> 
    
</head>

<body>

    <?php include "header.php"?>

    <div class="container-fluid">
        <div class="row">
            <div class="col-md-8 no-float bg-primary">
                New Technologies in Agriculture
            </div>
            <div class="col-md-4 no-float bg-danger">  
                News about agriculture growth
            </div>
        </div>
    </div>
    <footer>
        <p>© IIT Ropar Agriculture Advisor</p>
        <span>Site design by <a href="http://iitrpr.ac.in/" target="_blank">IIT Ropar</a></span>
    </footer>

</body>

</html>