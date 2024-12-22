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
        "SELECT username, email, age, balance FROM Users WHERE age != 60"
    )
    rows = cursor.fetchall()
    for row in rows:
        print(f"Имя: {row[0]} | Почта: {row[1]}| Возраст: {row[2]}| Баланс: {row[3]}")



