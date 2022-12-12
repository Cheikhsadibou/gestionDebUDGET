import cgi
import cgitb

cgitb.enable()
form = cgi.FieldStorage()

print("content-type: text/html; charset=utf-8\n")

html = """<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>Ma page web</title>
</head>
<body>
"""
print(html)

try:
  if form.getvalue("username"):
    username = form.getvalue("username")
    print(f"<p>Bonjour {username} !</p>")
  else:
      raise Exception("pseudo no transmit")
except:
    print("<p>pseudo non transmis</p>")

html = """
</body>
</html>
"""

print(html)