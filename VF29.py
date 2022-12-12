import http.server
import socketserver

port = 80
adress = ("", port)

handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(adress, handler)

print(f"le serveur a demarer sur le PORT {port}")

httpd.serve_forever()