import sqlite3 as sql

with sql.connect("not_telegram.db") as con:
    cursor = con.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
    )
    ''')

    for i in range(1, 11):
        cursor.execute(
            "INSERT INTO Users(username, email, age, balance) "
            "VALUES(?, ?, ?, ?)",
            (f'User{i}', f'example{i}@gmail.com', f'{10*i}', f'{1000}')
        )

    for i in range(1, 11, 2):
        cursor.execute(
            "UPDATE Users SET balance = ? WHERE username = ?",
            (500, f"User{i}")
        )

    for i in range(1, 11, 3):
        cursor.execute(
            "DELETE FROM Users WHERE username = ?",
            (f"User{i}", )
        )

    cursor.execute(
        "DELETE FROM Users WHERE id == 6",
    )

    cursor.execute(
        "SELECT COUNT(*) FROM Users"
    )

    total = cursor.fetchone()[0]

    cursor.execute(
        "SELECT SUM(balance) FROM Users"
    )
    _sum = cursor.fetchone()[0]

    print(_sum/total)

