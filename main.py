import socket
import threading
from user_data import add_user, authenticate_user

# Server Informationen
SERVER_HOST = '0.0.0.0'  # Setze die lokale IP für Tests
SERVER_PORT = 54321

# Erstelle einen Server-Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)

# Liste zum Speichern aller verbundenen Clients
clients = []
sessions = {}

def broadcast(message, sender_socket):
    """Sende die Nachricht an alle Clients außer dem Sender."""
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except BrokenPipeError:
                print(f"Fehler: Client-Verbindung unerwartet geschlossen (Broken pipe).")
                client.close()
                clients.remove(client)
            except Exception as e:
                print(f"Fehler beim Senden der Nachricht: {e}")
                client.close()
                clients.remove(client)

def handle_client(client_socket, client_address):
    """Verwaltet die Kommunikation mit einem verbundenen Client."""
    print(f"Neue Verbindung: {client_address}")
    clients.append(client_socket)  # Füge den Client zur Liste hinzu

    try:
        # Authentifizierung
        while True:
            client_socket.send("Bitte melden Sie sich mit 'login <username> <password>' oder 'register <username> <password>' an:\n".encode())
            message = client_socket.recv(1024).decode().strip()

            if message.startswith("register"):
                _, username, password = message.split()
                response = add_user(username, password)
                client_socket.send(response.encode())

            elif message.startswith("login"):
                _, username, password = message.split()
                if authenticate_user(username, password):
                    sessions[client_socket] = username  # Benutzer-Session speichern
                    client_socket.send(f"Willkommen {username}!\n".encode())
                    break
                else:
                    client_socket.send("Falscher Benutzername oder Passwort.\n".encode())
        
        # Haupt-Chat-Schleife nach erfolgreicher Anmeldung
        while True:
            message = client_socket.recv(1024)
            if not message or message.decode().lower() == "exit":
                print(f"{client_address} hat die Verbindung geschlossen.")
                break

            username = sessions.get(client_socket, "Unbekannt")
            formatted_message = f"{username}: {message.decode()}"
            broadcast(formatted_message.encode(), client_socket)

    except Exception as e:
        print(f"Fehler bei der Verbindung zu {client_address}: {e}")
    finally:
        client_socket.close()
        clients.remove(client_socket)
        print(f"Verbindung zu {client_address} geschlossen")

# Der Server akzeptiert und verwaltet Clients in Threads
print(f"Server läuft auf {SERVER_HOST}:{SERVER_PORT}")
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Neue Verbindung von {client_address}")
    
    # Starte einen neuen Thread, um den Client zu behandeln
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
