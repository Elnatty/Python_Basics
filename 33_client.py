import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c.connect(('localhost', 1234))

# when sending data to the server we must encode it.
c.send("Hello world".encode())

# receive message from servver
msg = c.recv(2048).decode()
print(msg)

# close connection.
c.close()