<?php
    /*
        Index Page
    */

    session_start();
    require_once "config.php";

    // Receive from form  and update database
    if(isset($_POST['title']) && isset($_POST['srcLink'])) {
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
                <h2>About Me</h2>
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
                        <a class="nav-link active" href="addArticle.php">Add Article</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="login.php">LogIn/Signup</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link disabled" href="#">Disabled</a>
                    </li>
                </ul>
                <hr class="d-sm-none">
            </div>
            <div class="col-sm-8">
                <h1>Add Article</h1>
                <form method="post">
                    <div class="form-group">
                        <label>Title</label>
                        <input type="text" name="title" class="form-control">
                    </div>    
                    <div class="form-group">
                        <label>Source Link</label>
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
                    <p>Don't have an account? <a href="signup.php">Sign Up here</a>.</p>
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
