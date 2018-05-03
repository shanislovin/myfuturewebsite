<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Failed Login!</title>
    <link rel="stylesheet" href="/static/style.css" type="text/css">
</head>

<!-- HEADER -->
<header>
    <h1>myfuture.com</h1>
</header>

<body>

<!-- NAVIGATION BAR -->
<nav>
    <ul>
        <li><a href="/">HOME</a></li>
        <li><a href="#jobs">JOBS</a></li>
        <li><a href="/views/about.html">About</a></li>
        <li><a href="#contact">CONTACT</a></li>
    </ul>
</nav>

<!-- form for failed login -->
<center>
    <div class="login_fail">
        <p>Login Failed, please try again:</p>
        <form action="/login" id="loginform" method="POST">
            Username: <input name='nick' input type="text"></li><br>
            Password: <input name='password' input type="password"></li><br>
            <button type="submit" class="submit">Login</button>
        </form>
    <div>
</center>

</body>

<!-- FOOTER: edited style to keep footer at bottom of page -->
<footer style="bottom:0; position:absolute; width:100%">
    <center>
        <div class="wrapper_f">
            <p class="footer_title">terms & conditions</p>
            <p class="footer_title"> contact us</p>
            <p>phone: <a href="tel:+61412345678"> +614 1234 5678</a></p>
            <p>email: <a href="mailto:helpme@future.com">helpme@future.com</a>.</p></div>
    </center>
</footer>

</html>