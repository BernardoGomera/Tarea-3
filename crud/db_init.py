import sqlite3

def init_db(path):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        correo TEXT,
        nota REAL
    )
    ''')
    # Insertar ejemplo
    cur.execute("INSERT INTO students (nombre, correo, nota) VALUES (?, ?, ?)", ("Carlos Pérez", "carlos@example.com", 85))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db('database.db')
