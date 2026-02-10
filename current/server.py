import sqlite3
import hashlib
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen()

def handle_client(client_socket):
    client_socket.send("Username: ".encode())
    username = client_socket.recv(1024).decode().strip()
    client_socket.send("Password: ".encode())
    password = client_socket.recv(1024).decode().strip()
    password = hashlib.sha256(password.encode()).hexdigest()

    conn = sqlite3.connect('sample.db')
    c = conn.cursor()
    c.execute("SELECT * FROM userdatabase WHERE username = ? AND password = ?", (username, password))
    if c.fetchone():
        client_socket.send("Login successful!".encode())
    else:
        client_socket.send("Login failed!".encode())
    conn.close()

while True:
    client_socket, addr = server.accept()
    threading.Thread(target=handle_client, args=(client_socket,)).start()