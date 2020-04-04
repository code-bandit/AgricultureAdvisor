<?php
    /*
        Sign Up Page
    */

    session_start();
    require_once 'config.php';

    if(isset($_SESSION['user'])) {
        header('Location: login.php');
    }

    $usernameAvailable = true;
    $passwordPossible = true;
    $confirmPassCorrect = true;

    if(isset($_POST['username']) && isset($_POST['password'])){
        $username = $_POST['username'];
        $password = hash('sha256', $_POST['password']);
        $confirmPassword = hash('sha256', $_POST['confirm_password']);
        
        //Check for Password correctness
        $passLen = strlen($_POST['password']);
        if($passLen < 4) {
            $passwordPossible = false;
        }

        //Check if confirmed password is same
        if($confirmPassword != $password) {
            $confirmPassCorrect = false;
        }

        //Check if $username is present in database
        $query = "SELECT * FROM users WHERE users.username = '$username'";
        $result = pg_query($conn, $query);
        $row = pg_fetch_row($result);

        if($row[1] == $username) {
            $usernameAvailable = false;
        }

        if($usernameAvailable and $passwordPossible and $confirmPassCorrect) {
            $query = "INSERT INTO users(id, username, password) values(default, '$username', '$password')";
            pg_query($conn, $query);
            header('Location: login.php');
        }
    }
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <title>Sign Up</title>
    <link rel="stylesheet" type="text/css" href="css/signup.css">

    <meta charset="UTF-8">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"/>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script> 

</head>
<body>
    
    <!-- Header for page -->
    <?php include "header.php"?>

    <!-- Form for signup -->
    <div class="wrapper">
        <h2>Sign Up</h2>
        <p>Please fill this form to create an account.</p>
        <form method="post">
            <div class="form-group">
                <?php
                    if(!$usernameAvailable) {
                        $htmlCode = <<<eod
                            <h4 style="color: red;">Username Not Available</h4>
eod;
                        echo $htmlCode;
                    }
                ?>
                <label>Username</label>
                <input type="text" name="username" class="form-control">
            </div>    
            <div class="form-group">
                <?php
                    if(!$passwordPossible) {
                        $htmlCode = <<<eod
                            <h4 style="color: red;">Password must be longer than 4 Characters</h4>
eod;
                        echo $htmlCode;
                    }
                ?>
                <label>Password</label>
                <input type="password" name="password" class="form-control">
            </div>
            <div class="form-group">            
                <?php
                    if(!$confirmPassCorrect) {
                        $htmlCode = <<<eod
                            <h4 style="color: red;">Password and Confirm Password not same</h4>
eod;
                        echo $htmlCode;
                }
                ?>
                <label>Confirm Password</label>
                <input type="text" name="confirm_password" class="form-control">
            </div>
            <div class="form-group">
                <input type="submit" class="btn btn-primary" value="Submit">
                <input type="reset" class="btn btn-default" value="Reset">
            </div>
            <p>Already have an account? <a href="login.php">Login here</a>.</p>
        </form>
    </div>    
    
    <script src="js/header.js"></script>
    
</body>
</html>