<?php
    /*
        Logout Page
    */

    session_start();
    if(!isset($_SESSION['user'])){
        header('Location: home.php');
    }

    unset($_SESSION['user']);
    session_unset();
    session_destroy();
    header('Location: index.php');
    exit;
?>