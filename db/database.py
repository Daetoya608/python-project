import sqlite3


def _connect_to_database(db: str = "db/marketplace.db") -> sqlite3.Connection:
    db_connect = sqlite3.connect(db)
    return db_connect

def _create_base_account_table(db: sqlite3.Connection) -> None:
    db.cursor().execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        phone TEXT NOT NULL,
        created_at TEXT NOT NULL
    )
    ''')

def _create_product_cards_table(db: sqlite3.Connection) -> None:
    db.cursor().execute('''
    CREATE TABLE IF NOT EXISTS product_cards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT DEFAULT '',
        purchase_count INTEGER DEFAULT 0,
        total_rating INTEGER DEFAULT 0,
        average_rating REAL DEFAULT 0
    )
    ''')



def _insert_to_users(db: sqlite3.Connection, email: str, phone: str, created_at: str) -> int:
    db.cursor().execute('INSERT INTO users (email, phone, created_at) VALUES (?, ?, ?)',
               (email, phone, created_at))
    return db.cursor().lastrowid

def _insert_to_product_cards(db: sqlite3.Connection, name: str, description: str) -> int:
    db.cursor().execute('INSERT INTO product_cards (name, description) VALUES (?, ?)',
                        (name, description))
    return db.cursor().lastrowid

def add_base_account(email: str, phone: str, created_at: str):
    db_conn = _connect_to_database()
    _create_base_account_table(db_conn)
    current_id = _insert_to_users(db_conn, email, phone, created_at)
    db_conn.commit()
    db_conn.close()
    return current_id

def add_product_card(name: str, description: str = "") -> int:
    db_conn = _connect_to_database()
    _create_product_cards_table(db_conn)
    current_id = _insert_to_product_cards(db_conn, name, description)
    db_conn.commit()
    db_conn.close()
    return current_id
