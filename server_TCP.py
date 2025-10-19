import socket
from AlphaBot import AlphaBot
import time

ADDRESS = ('0.0.0.0', 6969) #0.0.0.0 indirizzo ip speciale = this host(questo host)
MAX_CONNECTIONS = 3
BUFFER = 4096

ab = AlphaBot()
ab.stop() #OBBLIGATORIO

#creo un socket ipv4 udp
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#server quindi .bind
s.bind(ADDRESS)
s.listen(MAX_CONNECTIONS)
connection, sender_address = s.accept()

#metto in ascolto il server
message_bin = connection.recv(BUFFER)
#print(f"ho ricevuto {message_bin.decode()}")

# if(message_bin.decode()=="avanti"):
#     #print("Vado avanti")
#     alphabot.forward()
#     time.sleep(5)
#     alphabot.stop()

#USARE UNA VARIABILE AUSIILARIA PER TENER CONTO DELL'ULTIMO COMANDO PREMUTO E SE È UGUALE A
#QUELLO PREMUTO ORA LO IGNORO IN MODO TALE DA NON MANDARE TROPPI MESSAGGI UGUALI
while True:
    print(message_bin.decode())
    if(message_bin.decode()=="avanti"):
        ab.forward()
        message_bin = connection.recv(BUFFER)
    elif(message_bin.decode()=="indietro"):
        ab.backward()
        message_bin = connection.recv(BUFFER)
    elif(message_bin.decode()=="destra"):
        ab.right()
        message_bin = connection.recv(BUFFER)
    elif(message_bin.decode()=="sinistra"):
        ab.left()
        message_bin = connection.recv(BUFFER)
    elif(message_bin.decode()=="stop"):
        ab.stop()
        message_bin = connection.recv(BUFFER)

s.close()