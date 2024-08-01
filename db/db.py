import sqlite3


def create_database():
    con = sqlite3.connect("mandril.db")
    con.close()
