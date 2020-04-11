<?php
    /*
        Index Page
    */

    session_start();
    require_once "config.php";

    // Receive from form  and update database
    
    $srcLinkBool = false;
    $titleBool = false;
    if(isset($_POST['title']) && isset($_POST['srcLink'])) {
        if(empty($_POST['title'])) {
            $titleBool = true;
        }
        if(empty($_POST['srcLink'])) {
            $srcLinkBool = true;
        }
        if(!$titleBool && !$srcLinkBool) {
            $title = $_POST['title'];
            $srcLink = $_POST['srcLink'];
            $image = $_POST['img'];
            $description = $_POST['description'];
    
            $query = "INSERT INTO articles(id, title, srcLink, img, description) values(default, '$title', '$srcLink', '$image', '$description')";
            pg_query($conn, $query);
            if(isset($_SESSION['user'])) {
                header("Location: home.php");
            }else {
                header("Location: index.php");
            }
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
    
    <!-- Header for Page -->
    <?php include "header.php"?>
    
    <!-- Intro and Other Links -->
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
                <h3>Links</h3>
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
                    <?php
                        $htmlCode = <<<eod
                        <a class="nav-link" href="editProfile.php">Profile</a>
eod;
                        if(isset($_SESSION['user'])) {
                            echo $htmlCode;
                        }
                    ?>
                        
                    </li>
                    <li class="nav-item">
                        <a class="nav-link active" href="addArticle.php">Add Article</a>
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
            <!-- Add Article form -->
            <div class="col-sm-8">
                <h1>Add Article</h1>
                <form method="post">
                    <div class="form-group">
                    <?php
                            $htmlCode1 = <<<eod
                                <label>Title *</label>
eod;
                            $htmlCode2 = <<<eod
                                <label style="color: red;">Title *</label>
eod;
                            if($srcLinkBool) {
                                echo $htmlCode2;
                            }else {
                                echo  $htmlCode1;
                            }
                        ?>
                        <input type="text" name="title" class="form-control">
                    </div>    
                    <div class="form-group">
                    <?php
                            $htmlCode1 = <<<eod
                                <label>Source Link *</label>
eod;
                            $htmlCode2 = <<<eod
                                <label style="color: red;">Source Link *</label>
eod;
                            if($srcLinkBool) {
                                echo $htmlCode2;
                            }else {
                                echo  $htmlCode1;
                            }
                        ?>
                        <input type="link" name="srcLink" class="form-control"/>
                    </div>
                    <div class="form-group">
                        <label>Image</label>
                        <input type="file" name="img" class="form-control"/>
                    </div>
                    <div class="form-group">
                        <label>Description</label>
                        <input type="link" name="description" class="form-control"/>
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
