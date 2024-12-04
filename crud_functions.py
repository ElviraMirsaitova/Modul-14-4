import sqlite3


def initiate_db():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL)''')
    cursor.execute('DELETE FROM Products')
    for i in range(1,5):
        cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                       (f'Продукт {i}', f'Combi {i}', i))

    connection.commit()
    connection.close()

initiate_db()

def get_all_products():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    cursor.execute(" SELECT id, title, description, price FROM Products")
    products_db = cursor.fetchall()
    connection.commit()
    connection.close()
    return list(products_db)



