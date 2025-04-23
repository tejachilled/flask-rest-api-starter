import os
import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)

# Initialize database
conn = sqlite3.connect('items.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
cursor.execute("SELECT COUNT(*) FROM items")
if cursor.fetchone()[0] == 0:
    cursor.execute("INSERT INTO items (name) VALUES ('Sample Item 1')")
    cursor.execute("INSERT INTO items (name) VALUES ('Sample Item 2')")
    conn.commit()
conn.close()

@app.route('/items', methods=['GET'])
def get_items():
    conn = sqlite3.connect('items.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM items")
    rows = cursor.fetchall()
    conn.close()
    return jsonify([{"id": row[0], "name": row[1]} for row in rows])

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=False, host='0.0.0.0', port=port)
