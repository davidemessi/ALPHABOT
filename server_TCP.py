import socket
from AlphaBot import AlphaBot
import time
import sqlite3

ADDRESS = ('0.0.0.0', 8080) #0.0.0.0 indirizzo ip speciale = this host(questo host)
MAX_CONNECTIONS = 3
BUFFER = 4096

comandoPrecedente = 'stop'

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


while True:
    message_bin = connection.recv(BUFFER)
    comando = message_bin.decode().strip()
    print(f"comandoPrecedente = {comandoPrecedente}")
    print(f"messaggio ricevuto da client = {comando}")

    # se il comando è uguale al precedente, lo ignoro
    if comando == comandoPrecedente:
        continue

    # aggiorno comando precedente
    comandoPrecedente = comando

    if comando == "avanti":
        ab.forward()
    elif comando == "indietro":
        ab.backward()
    elif comando == "destra":
        ab.right()
    elif comando == "sinistra":
        ab.left()
    elif comando == "stop":
        ab.stop()
    elif comando == "quadrato":
        con = sqlite3.connect("./alphaBot_DB.db")
        cur = con.cursor()
        res = cur.execute(f"SELECT movimento FROM Comandi")
        movimenti = res.fetchall()
        #print(f"movimenti: {movimenti}")

        for riga in movimenti:
            movimento = riga[0]
            print(f"Eseguo: {movimento}")

            if movimento == "avanti":
                ab.forward()
            elif movimento == "indietro":
                ab.backward()
            elif movimento == "sinistra":
                ab.left()
            elif movimento == "destra":
                ab.right()
            elif movimento == "aspetta":
                time.sleep(1)

        ab.stop()
        con.close()

        #DA PROVARE SE FUNZIONA QUESTO CODICE CON IL DB

        

        

s.close()