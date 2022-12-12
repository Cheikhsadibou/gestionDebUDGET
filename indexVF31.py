"""
espires
path
comment
domain
secure
version
httponly
"""

import cgi

print("Set-Cookie: pref_lang=fr; httponly")
print("content-type: text/html; charset=utf-8\n")


html = """<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>Ma page web</title>
</head>
<body>
    <h1>Cookies avec python</h1>
"""
print(html)

print("<p>Bonjour !</p>")

html ="""
</body>
</html>

"""