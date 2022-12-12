import cgi
import http.server

"""
Set-Cookie: save_Data = Sadibou
expires
path
comment
domain
max-age
secure
httponly

"""

port = 80
adress = ("", port)

serveur = http.server.HTTPServer

handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]

httpd =serveur(adress, handler)


print(f"serveurà demarer sur le port {port}")


print("Set-Cookie: save_Data = Sadibou; httponly=true")

print("content-type: text/html; charset=utf-8\n")

html ="""

<!DOCTYPE html>
<head>
  <meta charset="UTF-8">
  <title>Ma page web</title>
</head>
<body>
     <h1>Cookies avec python</h1>
"""
  
print(html)

print("<p>Bonjour </p>")

html= """ 
</body>
</html>

"""


print(html)

httpd.serve_forever()