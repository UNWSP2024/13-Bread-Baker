# Name: Ariana Fafach
# Date: 4/30/2026
# Title: Program #2: Display Data from Cities Database


import sqlite3

def main():

    # Connect to the cities database:
    conn = sqlite3.connect('cities.db')

    # Create a cursor
    cur = conn.cursor()

    # Print a statement to say what the data is:
    print("Data from cities.db:")

    # Get all the data from the Cities table:
    cur.execute('SELECT * FROM Cities')
    results = cur.fetchall()

    # Print each row in the table:
    for row in results:
        print(f'{row[0]:<3}{row[1]:20}{row[2]:,.0f}')

    # Close the connection to the database:
    conn.close()

if __name__ == "__main__":
    main()