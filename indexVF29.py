import cgi

print("content-type: text/html; charchet=utf-8\n") 


html = """<!DOCTYPE html>
<head>
  <meta charset="UTF-8">
  <title>ma page web</title>
</head>
<body>
    <h1>page weg avec python CGI</h1>

    <form metod ="post" action="resultVF30.py">
        <p><input type="text" name="username">
        <input type="submit" value="Envoyer"></p>
    </form>
</body>
</html>

"""

print(html)