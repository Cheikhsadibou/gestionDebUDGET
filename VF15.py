"""
==>class str : string (chaine de caractaire )

==>str.upper() , str.lower(), str.capitalize(), str.title()
==>une metode de chaine travaille sur une copie,  et pas sur la chaine elle-meme

==>str.find(<chaine>, <debut>, <fin>)
   str.index(<chaine>, <debut>, <fin>)
==>str.strip()

==>str.re

==>str.replace(<encienne>, <nouvel>, <occurances>)

==>str.isalpha(), str.digit(), str.isdecimal(), str.isnumeric(), str.isalphanum()

str.islowwer(), str.isuper()

str.isidentifier(), str.iskeyword()

"""
ch = "le language python "

if "language" in  ch:
  print("trouver")
else:
  print("non trouver")