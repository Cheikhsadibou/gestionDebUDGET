import cgi

print("content-type: text/html; charset=utf-8\n")


html = """<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>Ma page web</title>
</head>
<body>
    <h1>Bonjour Cheikh !</h1>
    
      <form method="post" action="result.py">
          <p><input type="text" name="username">
          <input type="submit" value="Envoyer"></p>
      </form>
</body>
</html>

"""

print(html)