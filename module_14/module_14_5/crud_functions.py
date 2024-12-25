import sqlite3 as sql


def initiate_db():
    with sql.connect("Products.db") as c:
        cursor = c.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
        )
        ''')

        for i in range(1, 5):
            cursor.execute('''
                INSERT INTO Products(title, description, price) 
                VALUES (?, ?, ?)
                ''',
                (
                    f'Product{i}',
                    f'Круто x {i}',
                    f'{100 * i}',
                )
                           )
    with sql.connect("Users.db") as c:
        cursor = c.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users(
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER,
            balance INTEGER NOT NULL
            )
            ''')


def is_included(username):
    with sql.connect("Users.db") as c:
        cur = c.cursor()
        cur.execute(f'''
        SELECT username
        FROM Users
        WHERE username = "{username}"
        ''')
        if cur.fetchone():
            return False
        else:
            return True


def add_users(username, email, age):
    with sql.connect("Users.db") as c:
        cur = c.cursor()
        cur.execute(f'''
        INSERT INTO Users(username, email, age, balance)
        VALUES("{username}", "{email}", "{age}", "{1000}")
        ''')
        c.commit()


def get_all_products(num):
    with sql.connect("Products.db") as c:
        cur = c.cursor()
        cur.execute('''
            SELECT title, description, price 
            FROM Products 
            WHERE id = ?
        ''',
        (f"{num}",)
                    )
        row = cur.fetchone()
        result = f"Продукт: {row[0]} | Описание: {row[1]}| Стоимость: {row[2]}"
        return result
