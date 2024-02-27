<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsive Instagram</title>
    <link rel="stylesheet" href="stylesheet.css">
    <?php 
    $post_list=[];
    $post1=new stdClass();
    $post1->Username="Boss3y";
    $post1->image="img1.jpg";
    $post1->cite="Apa aja lah";
    $post_list[]=$post1;?>
</head>
<body>
    <header>
        <div class="logo"><img src="FOMO/2.png"></div>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">Explore</a></li>
                <li><a href="#">Profile</a></li>
            </ul>
        </nav>
    </header> 
    <?php
    for($i=0;$i<count($post_list);$i++){
        echo "<div class='tm-post'>";
        echo "<h2>" .$post_list[$i] -> Username."</h2>";
        echo "<img src=". $post_list[$i]-> image. ">";
        echo "<p>". $post_list[$i]->cite."</p>";
        echo "</div>";
    }?>
    <footer>
        <p>&copy; 2024 Instagram</p>
    </footer>
</body>
</html>

