<?php
    /*
        Login Page
    */

    session_start();
    require_once 'config.php';

    if(isset($_SESSION['user'])) {
        header('Location: home.php');
    }
	
	$admin = 'admin';

    if(isset($_POST['username']) && isset($_POST['password'])){
        $username = $_POST['username'];
        $password = hash('sha256', $_POST['password']);

        $query = "SELECT * FROM users WHERE users.username = '$username' AND users.password = '$password'";
        $result = pg_query($conn, $query);
        $row = pg_fetch_row($result);

        // echo $row[1];   
        // echo $result;

        if($row[1] != $username or $row[2] != $password){
            echo "fail";
        } else{
			$_SESSION['user'] = $row[0];
            if($username == $admin){
                header('Location: admin.php');
            }else{
                header('Location: home.php');
            }
        }
    }
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <title>Login</title>
    <link rel="stylesheet" type="text/css" href="css/login.css"/>
    
    <meta charset="UTF-8"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"/>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script> 
</head>
<body>
    <?php include "header.php"?>
    <div class="wrapper">
        <h2>Login</h2>
        <p>Please fill this form to create an account.</p>
        <form method="post">
            <div class="form-group">
                <label>Username</label>
                <input type="text" name="username" class="form-control">
            </div>    
            <div class="form-group">
                <label>Password</label>
                <input type="password" name="password" class="form-control"/>
            </div>
            <div class="form-group">
                <input type="submit" class="btn btn-primary" value="Submit">
                <input type="reset" class="btn btn-default" value="Reset">
            </div>
            <p>Don't have an account? <a href="signup.php">Sign Up here</a>.</p>
        </form>
    </div>    
</body>
</html>