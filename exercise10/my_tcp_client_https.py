import socket, ssl

HOST = 'color.adobe.com'
PORT = 443

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket = context.wrap_socket(client, server_hostname=HOST)
client_socket.connect((HOST, PORT))

client_socket.send(b'GET / HTTP/1.1\r\nHost: color.adobe.com\r\n\r\n')

while True:
    response = client_socket.recv(4096)
    if (len(response) < 1):
        break
    print(response.decode('utf-8'))

client.close()
