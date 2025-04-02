import socket

HOST ='httpforever.com'
PORT= 80

#socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect client
client.connect((HOST, PORT))

#send some data
client.send(b"GET / HTTP/1.1\r\nHost: httpforever.com\r\n\r\n")


#receive data
response = client.recv(4096)

print(response.decode('utf-8'))
client.close()
