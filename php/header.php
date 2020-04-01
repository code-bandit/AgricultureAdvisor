<nav class="navbar navbar-expand-sm bg-dark navbar-dark sticky-top" id="navbar">
    <a class="navbar-brand" href="#" style="font-family: georgia,garamond,serif;font-size:16px;font-style:italic;">Agriculture Advisor</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="collapsibleNavbar">
        <ul class="navbar-nav">
        <li class="nav-item active">
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
        <li class="nav-item active">
            <a class="nav-link" href="#">About Us</a>
        </li>
        <?php
                if(isset($_SESSION['user'])){
                    echo '<li class="nav-item active"><a href="logout.php" class="nav-link">'.'LogOut'.'</a></li>';
                }else{
                    echo '<li class="nav-item active"><a href="login.php" class="nav-link">'.'LogIn / SignUp'.'</a></li>';
                }
            ?> 
        </ul>
    </div> 

    <!-- TODO: this is written like this for future edits -->
    <?php
        $htmlCode = <<<eod
            <form class="form-inline" action="search.php">
            <input class="form-control mr-sm-2" type="text" placeholder="Search">
            <button class="btn btn-success" type="submit">Search</button>
            </form>
eod;
        if(isset($_SESSION['user'])) {
            echo $htmlCode;
        }else {
            echo $htmlCode;
        }
    ?>
</nav>