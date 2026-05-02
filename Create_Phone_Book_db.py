# Name: Ariana Fafach
# Date: 4/30/2026
# Title: Program #3


import sqlite3

def create_database():

    conn = sqlite3.connect('phone_book.db')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS Entries (ID INTEGER PRIMARY KEY NOT NULL, name TEXT, phone_number TEXT)''')
    cur.execute('''INSERT INTO Entries (name, phone_number) Values (?,?)''', ("John Smith", "111-111-1111"))
    cur.execute('''INSERT INTO Entries (name, phone_number) Values (?,?)''', ("Sally Young", '222-222-2222'))
    cur.execute('''INSERT INTO Entries (name, phone_number) Values (?,?)''', ("Sam Fuller", '666-666-6666'))
    cur.execute('''INSERT INTO Entries (name, phone_number) Values (?,?)''', ("Kate Nelson", '777-777-7777'))
    cur.execute('''INSERT INTO Entries (name, phone_number) Values (?,?)''', ("Slim Pickens", '303=303-3030'))
    cur.execute('''INSERT INTO Entries (name, phone_number) Values (?,?)''', ("Nancy Peters", '200-300-2030'))
    cur.execute('''INSERT INTO Entries (name, phone_number) Values (?,?)''', ("Bob Jones", '999-999-9999'))
    cur.execute('''INSERT INTO Entries (name, phone_number) Values (?,?)''', ("Rick Burr", '900-800-9080'))
    
    conn.commit()
    conn.close()
    
if __name__ == '__main__':
    create_database()