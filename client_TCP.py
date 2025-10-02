import socket
from pynput import keyboard


SERVER_ADRS = ("192.168.1.113", 6969)
BUFFER = 4096

#creo un socket ipv4 udp
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# msg = input("Inserisci un messaggio: ")
# s.connect(SERVER_ADRS)
# s.send(msg.encode())
# data = s.recv(BUFFER)
# print(data.decode())


def on_press(key):
    try:
        if key.char == 'w':  # avanti
            print("Avanti")
            s.send("avanti")
        elif key.char == 's':  # indietro
            print("Indietro")
            s.send("indietro")
        elif key.char == 'a':  # sinistra
            print("Sinistra")
            s.send("sinistra")
        elif key.char == 'd':  # destra
            print("Destra")
            s.send("destra")
    except AttributeError:
        # qui entrano i tasti speciali, tipo frecce o shift
        pass

def on_release(key):
    # quando rilascio un tasto → stop
    print("Stop")
    s.send("stop")
    if key == keyboard.Key.esc:
        # se premi ESC chiudi il programma
        return False

# attiva il listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

s.close()