<?php
    /*
        Home Page
    */

    session_start();
    require_once "config.php";
?>

<!DOCTYPE html>
<html lang="en">
<head>

    <title>Home Page</title> 
    <link rel="stylesheet" type="text/css" href="css/index.css">

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
    
    <div class="jumbotron text-center" style="margin-bottom:0">
        <h1>Agriculture Advisor</h1>
        <p>Made By students of IIT Ropar</p> 
    </div>
    
    <?php include "header.php"?>
    
    <div class="container" style="margin-top:100px">
        <div class="row">
            <div class="col-sm-4" id="sidemenu">
                <?php
                    $userId = $_SESSION['user'];
                    $query = "SELECT * FROM users WHERE users.id = '$userId'";
                    $row = pg_fetch_row(pg_query($conn, $query));
                    $row[1] = strtoupper($row[1]);
                    $htmlCode = <<<eod
                                    <h3> Welcome $row[1] </h3>
eod;
                    echo $htmlCode;
                ?>
                <div class="fakeimgAboutme"></div>
                <br>
                <p>IIT Ropar is a leading Institute in agriculture related researches..</p>
                <?php
                    $userId = $_SESSION['user'];
                    $query = "SELECT * FROM profileUser where profileUser.id = '$userId'";
                    $row = pg_fetch_row(pg_query($conn, $query));
                    $htmlCode = <<<eod
                        <div>
                            <h3> Profile </h3>
                            <p><b>Soli Type :</b> $row[1]</p>
                            <p><b>Soli Ph :</b> $row[2]</p>
                            <p><b>State :</b> $row[3]</p>
                            <p><b>District :</b> $row[4]</p>
                            <p><b>Village :</b> $row[5]</p>
                            <p><b>Weather :</b> $row[6]</p>
                        </div>
eod;
                    echo $htmlCode;
                ?>
                <h3>Links</h3>
                <ul class="nav nav-pills flex-column" id="linksIndexPage">
                    <li class="nav-item">
                        <?php
                            $htmlCode1 = <<<eod
                                <a class="nav-link active" href="home.php">Home</a>
eod;

                            $htmlCode2 = <<<eod
                                <a class="nav-link active" href="index.php">Home</a>
eod;
                            if(isset($_SESSION['user'])) {
                                echo $htmlCode1;
                            }else {
                                echo $htmlCode2;
                            }
                        ?>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="editProfile.php">Profile</a>
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
                
            <?php
                    $query = "SELECT * FROM articles";
                    $result = pg_query($conn, $query);
                    if(!$result) {
                        echo "No articles available";
                    }else {
                        while($row = pg_fetch_row($result)) {
                            $row[1] = strtoupper($row[1]);
                            $row[5] = date("M d, Y", strtotime($row[5])); 
                            $htmlCode = <<<eod
                                <h2><a href="$row[2]" style="text-decoration: none; color: black;">$row[1]</a></h2>
                                <h5>$row[5]</h5>
                                <div class="fakeimg">Fake Image</div>
                                <p>$row[4]</p>
                                <br>
eod;
                            echo $htmlCode;
                        }
                    }
                ?>
            </div>
        </div>
    </div>
    
    <footer>
        <p>© IIT Ropar Agriculture Advisor</p>
    </footer>
    
    <!-- <script type="text/javascript" src="js/index.js"></script> -->
    <script type="text/javascript" src="js/header.js"></script>
    
</body>
</html>