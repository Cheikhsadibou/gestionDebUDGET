import http.server

port = 80
adress = ("", port)

serveur = http.server.HTTPServer

handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]

httpd =serveur(adress, handler)


print(f"serveurà demarer sur le port {port}")
httpd.serve_forever()