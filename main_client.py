import socket
import threading
from chat_data import add_message

# Server-Details
SERVER_HOST = '127.0.0.1'  #IP-Adresse des Servers
SERVER_PORT = 12345        #Port auf dem der Client die Verbindung zum Server herstellt

# Erstelle einen Client-Socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Erstellt einen neuen Client-Socket mit IPv4 (AF_INET) und dem TCP-Protokoll (SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))#Der Client-Socket verbindet sich mit dem Server

def receive_messages():
    """Empfängt Nachrichten vom Server."""
    while True:
        try:
            message = client_socket.recv(1024).decode()#recv(1024) bedeutet, dass bis zu 1024 Bytes empfangen werden. Die empfangenen Daten werden dann mit decode() von Bytes in einen String umgewandelt.
            if message:
                print(message)
            else:
                print("Server hat die Verbindung geschlossen.")
                client_socket.close()
                break
        except:
            print("Verbindung zum Server verloren.")
            client_socket.close()
            break

def send_messages():
    """Sende Nachrichten an den Server."""
    while True:
        message = input("")
        if message.lower() == "exit":
            client_socket.send("exit".encode())#Die Nachricht wird mit encode() in Bytes umgewandelt, um über das Netzwerk gesendet werden zu können.
            client_socket.close()
            break
        client_socket.send(message.encode())
        add_message(message)

# Starte zwei Threads: einen zum Empfangen und einen zum Senden von Nachrichten
receive_thread = threading.Thread(target=receive_messages)#Erstellt einen neuen Thread für das Empfangen von Nachrichten. Die target-Funktion (receive_messages) wird in diesem Thread ausgeführt.
receive_thread.start()

send_thread = threading.Thread(target=send_messages)#Erstellt einen zweiten Thread für das Senden von Nachrichten. Auch hier wird die send_messages-Funktion in einem separaten Thread ausgeführt.
send_thread.start()
