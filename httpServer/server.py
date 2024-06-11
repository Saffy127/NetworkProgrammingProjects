import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

PORT = 8000

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        data = [{"id": row[0], "name": row[1], "age": row[2]} for row in rows]
        conn.close()

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = json.loads(self.rfile.read(content_length))
        name = post_data['name']
        age = post_data['age']

        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
        conn.commit()
        conn.close()

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"message": "User added"}).encode())

    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        put_data = json.loads(self.rfile.read(content_length))
        user_id = put_data['id']
        name = put_data.get('name')
        age = put_data.get('age')

        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        if name:
            cursor.execute("UPDATE users SET name = ? WHERE id = ?", (name, user_id))
        if age:
            cursor.execute("UPDATE users SET age = ? WHERE id = ?", (age, user_id))
        conn.commit()
        conn.close()

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"message": "User updated"}).encode())

    def do_DELETE(self):
        content_length = int(self.headers['Content-Length'])
        delete_data = json.loads(self.rfile.read(content_length))
        user_id = delete_data['id']

        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        conn.close()

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"message": "User deleted"}).encode())

    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        put_data = json.loads(self.rfile.read(content_length))
        user_id = put_data['id']
        name = put_data.get('name')
        age = put_data.get('age')

        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        if name:
            cursor.execute("UPDATE users SET name = ? WHERE id = ?", (name, user_id))
        if age:
            cursor.execute("UPDATE users SET age = ? WHERE id = ?", (age, user_id))
        conn.commit()
        conn.close()

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"message": "User updated"}).encode())

if __name__ == "__main__":
    # Initialize the database
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       age INTEGER NOT NULL)''')
    conn.commit()
    conn.close()

    server_address = ('', PORT)
    httpd = HTTPServer(server_address, MyHandler)
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
