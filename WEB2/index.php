<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsive Instagram</title>
    <link rel="stylesheet" href="stylesheet.css">
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
    $post_list=[];
    $post1=new stdClass();
    $post1->caption="caption";
    $post1->image="image.jpg";
    $post_list[]=$post1;

    for($i=0;$i<count($post_list);$i++){
        echo "<div class='tm-post'>";
        echo "<h2>" .$post_list[$i] -> caption."</h2>";
        echo "<img src=". $post_list[$i]-> image. ">";
        echo "</div";
    }?>
        <div class="post">
            <img src="img2.jpg  " alt="Post Image">
            <div class="post-details">
                <h2>Post Title</h2>
                <p>Posted by User123</p>
                <p>monkey</p>
            </div>
        </div>
        <!-- More posts... -->
        <div class="post">
            <img src="img1.jpg  " alt="Post Image">
            <div class="post-details">
                <h2>Post Title</h2>
                <p>Posted by User123</p>
                <p>Car.</p>
            </div>
        </div>
   

    <footer>
        <p>&copy; 2024 Instagram</p>
    </footer>
</body>
</html>


