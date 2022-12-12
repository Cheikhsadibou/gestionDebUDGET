# app.py
import sqlite3

print("Application de Gestion de contacte avec Python et Sqlite3")

with sqlite3.connect("cont@ct.db") as connection:
    cursor = connection.cursor()


def create_table():
    cursor.execute(
        "CREATE TABLE cont@ct (id INTEGER PRIMARY KEY AUTOINCREMENT,nomComplet TEXT, email TEXT, telephone TEXT)")


def ajouter_contacte():
    cursor.execute(
        "INSERT INTO contacte(nomComplet, email, telephone) VALUES('Ousseynou DIOP', 'ous@fakemail.com', '763887835')")
    cursor.execute(
        "INSERT INTO contacte(nomComplet, email, telephone) VALUES('Bamba Sall', 'bamba@fakemail.com', '763887825')")
    cursor.execute(
        "INSERT INTO contacte(nomComplet, email, telephone) VALUES('Awa DIOP', 'awa@fakemail.com', '763882835')")
    connection.commit()
def afficher_les_contactes():
    rows = cursor.execute("SELECT * FROM contacte").fetchall()
    print(rows)


def afficher_un_contacte():
    row = cursor.execute(
        "SELECT * FROM contacte WHERE telephone = 763887825").fetchone()
    print(row)


def supprimer_contacte():
    telephone = "763882835"
    cursor.execute(
        "DELETE FROM contacte WHERE telephone = ?",
        (telephone,)
    )
    connection.commit()


def modifier_contacte():
    nouveau_numero = "76332982"
    ancien_numero = "763887825"
    cursor.execute(
        "UPDATE contacte SET telephone = ? WHERE telephone = ?",
        (nouveau_numero, ancien_numero)
    )
    connection.commit()