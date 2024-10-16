# Chat-Server README

## Überblick

Dieser Chat-Server bietet eine einfache Möglichkeit, mehrere Clients gleichzeitig zu verbinden und Nachrichten untereinander auszutauschen. Er enthält Benutzerregistrierung und -anmeldung sowie Nachrichtenverlauf, der in einer SQLite-Datenbank gespeichert wird.

## Voraussetzungen

- Python 3.x
- `socket`-Modul (standardmäßig in Python enthalten)
- `threading`-Modul (standardmäßig in Python enthalten)
- `SQLAlchemy`-Modul zur Datenbankanbindung

## Installation

1. Klonen oder laden Sie dieses Repository herunter.
2. Installieren Sie alle benötigten Python-Abhängigkeiten:

   ```bash
   pip install sqlalchemy


## Verwendung

`Server`

Starten Sie den Server:


```bash
python main.py
```
Der Server läuft standardmäßig auf 127.0.0.1:12345. Sie können die IP-Adresse und den Port nach Bedarf im Code ändern.

Der Server verwaltet mehrere Clients gleichzeitig und ermöglicht die Kommunikation über Threads. Wenn ein Client eine Nachricht sendet, wird diese an alle verbundenen Clients weitergeleitet.

`Client`

Verbinden Sie sich mit dem Server, indem Sie den Client ausführen:

``` bash
python main_client.py
```
Nach dem Start des Clients können Sie sich entweder registrieren oder anmelden:

- Registrierung:

```bash
register <username> <password>
```
- Anmeldung:

```bash
login <username> <password>
```
Sobald Sie angemeldet sind, können Sie Nachrichten an den Chat senden. Alle Nachrichten werden an alle verbundenen Clients gesendet.

Um die Verbindung zu beenden, geben Sie exit ein.

`Funktionen`

- Registrierung und Anmeldung: Benutzer können sich registrieren und mit ihren Anmeldeinformationen anmelden.

- Nachrichtenverlauf: Jede Nachricht wird zusammen mit einem Zeitstempel in der SQLite-Datenbank gespeichert.
