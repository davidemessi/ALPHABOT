import socket

SERVER_ADRS = ("192.168.1.113", 6969)
BUFFER = 4096

#creo un socket ipv4 udp
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

msg = input("Inserisci un messaggio: ")
s.connect(SERVER_ADRS)
s.send(msg.encode())
data = s.recv(BUFFER)
print(data.decode())

s.close()