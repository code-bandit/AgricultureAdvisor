<nav class="navbar navbar-expand-sm bg-dark navbar-dark navbar-fixed-top" rolle="navigation">
    <form class="form-inline" action="search.php">
        <input class="form-control mr-sm-2" type="text" placeholder="Search">
        <button class="btn btn-success" type="submit">Search</button>
    </form>
    <ul class="navbar-nav ml-auto">
        <?php
            if($_SESSION['user']){
                echo '<li class="nav-item active"><a href="logout.php" class="nav-link" style="float:right;">'.'LogOut'.'</a></li>';
            }else{
                echo '<li class="nav-item active"><a href="login.php" class="nav-link" style="float:right;">'.'LogIn / SignUp'.'</a></li>';
            }
        ?> 
    </ul>
</nav>