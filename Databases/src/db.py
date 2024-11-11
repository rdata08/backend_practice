import sqlite3

def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getinstance


class DatabaseDriver(object):
    """
    Database driver for the Venmo (Full) app.
    Handles with reading and writing data with the database.
    """

    def __init__(self):
        self.conn = sqlite3.connect("venmo.db", check_same_thread=False)
        self.create_user_table()

    def create_user_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS user(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            username TEXT NOT NULL,
            balance INTEGER NOT NULL
        );""")

    def delete_user_table(self):
        self.conn.execute("""
        DROP TABLE IF EXISTS user;
        """)
    
    def get_all_users(self):
        cursor = self.conn.execute("SELECT * FROM user;")
        tasks = []
        for row in cursor:
            tasks.append({"id": row[0], "name": row[1], "username": row[2]})
        return tasks

    def insert_user_table(self, name, username, balance):
        cursor = self.conn.execute("""
        INSERT INTO user(name, username, balance) VALUES (?, ?, ?);
        """, (name, username, balance))
        self.conn.commit()
        return cursor.lastrowid

    def get_user_by_id(self, user_id):
        cursor = self.conn.execute("SELECT * FROM user WHERE id = ?;", (user_id,))
        for row in cursor:
            return ({"id": row[0], "name": row[1], "username": row[2], "balance": row[3]})
        return None

    def delete_user_by_id(self, id):
        self.conn.execute("""DELETE FROM user WHERE id=?""", (id,))

    def update_user_balance_by_id(self, new_balance, id):
        self.conn.execute("""
        UPDATE user SET balance = ?,
        WHERE id = ?
        """, (new_balance, id))
        self.conn.commit()
        
        

# Only <=1 instance of the database driver
# exists within the app at all times
DatabaseDriver = singleton(DatabaseDriver)