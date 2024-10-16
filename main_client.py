import socket
import threading
from chat_data import add_message

# Server-Details
SERVER_HOST = '127.0.0.1'  # Stelle sicher, dass dies die IP des Servers ist
SERVER_PORT = 12345

# Erstelle einen Client-Socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

def receive_messages():
    """Empfängt Nachrichten vom Server."""
    while True:
        try:
            message = client_socket.recv(1024).decode()
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
            client_socket.send("exit".encode())
            client_socket.close()
            break
        client_socket.send(message.encode())
        add_message(message)

# Starte zwei Threads: einen zum Empfangen und einen zum Senden von Nachrichten
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()
