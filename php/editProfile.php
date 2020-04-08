<?php
    /*
        Index Page
    */

    session_start();
    require_once "config.php";

    // Receive from form  and update database
    $soilTypeMentioned = true;
    $weatherMentioned = true;
    
    if(isset($_POST['soilType']) || isset($_POST['weather'])) {
        if(isset($_POST['soilType'])) {
            $soilTypeMentioned = false;
        }
        if($_POST['weather'] == "blank") {
            $weatherMentioned = false;
        }
        if(!$soilTypeMentioned && $weatherMentioned){
            $soilType = $_POST['soilType'];
            $soilPh = $_POST['soilPh'];
            $state = $_POST['state'];
            $district = $_POST['district'];
            $village = $_POST['village'];
            $weather = $_POST['weather'];
            $username = $_SESSION['user'];
            $query = "SELECT * FROM profileUser WHERE profileUser.id = '$username'";
            $row = pg_fetch_row(pg_query($conn, $query));
            if($row) {
                $query = "DELETE FROM profileUser where profileUser.id = '$username'";
                pg_query($conn, $query);
                $query = "INSERT INTO profileUser(id, soilType, soilPh, state, district, village, weather) values('$username', '$soilType', '$soilPh', '$state', '$district', '$village', '$weather')";
                pg_query($conn, $query);
            }else {
                $query = "INSERT INTO profileUser(id, soilType, soilPh, state, district, village, weather) values('$username', '$soilType', '$soilPh', '$state', '$district', '$village', '$weather')";
                pg_query($conn, $query);
            }
            header('Location: home.php');
        }
    }


?>

<!DOCTYPE html>
<html lang="en">
<head>

    <title>Add Article</title> 
    <link rel="stylesheet" type="text/css" href="css/addArticle.css">

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
    <style>
        .fakeimg {
            height: 200px;
            background: #aaa;
        }
        </style>
</head>
<body>
    
    <!-- <div class="jumbotron text-center" style="margin-bottom:0">
        <h1>Agriculture Advisor</h1>
        <p>Made By students of IIT Ropar</p> 
    </div> -->
    
    <?php include "header.php"?>
    
    <div class="container" style="margin-top:40px">
        <div class="row">
            <div class="col-sm-4" id="sidemenu">
            <?php
                    if(isset($_SESSION['user'])) {
                        $userId = $_SESSION['user'];
                        $query = "SELECT * FROM users WHERE users.id = '$userId'";
                        $row = pg_fetch_row(pg_query($conn, $query));
                        $row[1] = strtoupper($row[1]);
                        $htmlCode = <<<eod
                                        <h3> Welcome $row[1] </h3>
eod;
                        echo $htmlCode;
                    }else {
                        $htmlCode = <<<eod
                                         <h2>About IIT ROPAR</h2>
eod;
                        echo $htmlCode;
                    }
                ?>
                <div class="fakeimgAboutme"></div>
                <br>
                <p>IIT Ropar is a leading Institute in agriculture related researches..</p>
                <h3>Some Links</h3>
                <p>Lorem ipsum dolor sit ame.</p>
                <ul class="nav nav-pills flex-column" id="linksIndexPage">
                    <li class="nav-item">
                        <?php
                            $htmlCode1 = <<<eod
                                <a class="nav-link" href="home.php">Home</a>
eod;

                            $htmlCode2 = <<<eod
                                <a class="nav-link" href="index.php">Home</a>
eod;
                            if(isset($_SESSION['user'])) {
                                echo $htmlCode1;
                            }else {
                                echo $htmlCode2;
                            }
                        ?>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link active" href="editProfile.php">Profile</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="addArticle.php">Add Article</a>
                    </li>                    
                    <li class="nav-item">
                        <a class="nav-link" href="recommend.php">Get Recommendation</a>
                    </li>
                    <?php
                        if(isset($_SESSION['user'])){
                            echo '<li class="nav-item active"><a href="logout.php" class="nav-link">'.'LogOut'.'</a></li>';
                        }else{
                            echo '<li class="nav-item active"><a href="login.php" class="nav-link">'.'LogIn / SignUp'.'</a></li>';
                        }
                    ?> 
                </ul>
                <hr class="d-sm-none">
            </div>
            <div class="col-sm-8">
                <h1>Edit Profile</h1>
                <form method="post">
                    <div class="form-group">
                        <?php
                            $htmlCode1 = <<<eod
                                <label>Soil Type *</label>
eod;
                            $htmlCode2 = <<<eod
                                <label style="color: red;">Soil Type *</label>
eod;
                            if(!$soilTypeMentioned) {
                                echo $htmlCode2;
                            }else {
                                echo  $htmlCode1;
                            }
                        ?>
                        <input type="text" name="soilType" class="form-control"/>
                    </div>
                    <div class="form-group">
                        <label>Soil Ph</label>
                        <input type="text" name="soilPh" class="form-control"/>
                    </div>
                    <div class="form-group">
                        <label>State</label>
                        <input type="text" name="state" class="form-control">
                    </div>    
                    <div class="form-group">
                        <label>Village</label>
                        <input type="text" name="village" class="form-control">
                    </div>    
                    <div class="form-group">
                        <label>District</label>
                        <input type="text" name="district" class="form-control">
                    </div>    
                    <div class="form-group">
                        <?php
                            $htmlCode1 = <<<eod
                                <label>Weather *</label>
eod;
                            $htmlCode2 = <<<eod
                                <label style="color: red;">Weather *</label>
eod;
                            if(!$weatherMentioned) {
                                echo $htmlCode2;
                            }else {
                                echo  $htmlCode1;
                            }
                        ?>
                        <select id="weather" name="weather" class="form-control">
                            <option value="blank"></option>
                            <option value="good">Good</option>
                            <option value="hot">Hot</option>
                            <option value="humid">Humid</option>
                            <option value="bad">Bad</option>
                        </select> 
                    </div>
                    <div class="form-group">
                        <input type="submit" class="btn btn-primary" value="Submit">
                        <input type="reset" class="btn btn-default" value="Reset">
                    </div>
                </form>
            </div>
        </div>
    </div>
    
    <footer>
        <p>© IIT Ropar Agriculture Advisor</p>
    </footer>
    
    <!-- <script type="text/javascript" src="js/header.js"></script> -->
    
</body>
</html>
