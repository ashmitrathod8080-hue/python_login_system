import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

# Receive and display username prompt
message = client.recv(1024).decode()
print(message, end='', flush=True)
username = input()
client.send(username.encode())

# Receive and display password prompt
message = client.recv(1024).decode()
print(message, end='', flush=True)
password = input()
client.send(password.encode())

# Receive and display result
result = client.recv(1024).decode()
print(result)