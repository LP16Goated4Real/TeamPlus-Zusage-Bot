# :goat:LP16's brilliantes TeamPlus auto Zusage Skript:goat:
Unterstützt wird nur Windows OS.
## Inhaltsverzeichnis :fire::fire::fire:

 1. [Voraussetzungen](#voraussetzungen)
    - [Python](#python):snake:
 2. [Installation](#installation)
    - [Option 1: ZIP](#option-1-zip)
    - [Option 2: Git Clone](#option-2-git-clone)
 3. [How-to](#how-to)
    - [Konfiguration](#konfiguration)
    - [Sprüche konfigurieren](#sprüche-konfigurieren)
    - [Windows Task Scheduler](#windows-task-scheduler)
    - [Manuell starten](#manuell-starten)
---
### <ins>Voraussetzungen</ins>:
#### **Python**
Gehe zur [offiziellen Python-Website](https://www.python.org/downloads/) und installiere den Python-Installer.\
**Wichtig**:
1. Version 3.14 oder neuer auswählen
2. "Python zu PATH hinzufügen" ankreuzen
3. Sicherstellen, dass **pip** und **venv** installiert sind
4. Optional: "Launcher für alle Benutzer installieren"
---
### <ins>Installation</ins>
#### Option 1: ZIP
Der einfachste Weg ist der Download per ZIP. Dafür auf der [TeamPlus-Zusage-Bot Seite](https://github.com/LP16Goated4Real/TeamPlus-Zusage-Bot) zuerst den grünen **code** Knopf und danach auf **Download ZIP** klicken.
Speichere die ZIP-Datei anschließend an einem beliebigen Ort.
#### Option 2: Git Clone
Hierfür muss zuerst [Git](https://www.youtube.com/watch?v=t2-l3WvWvqg) installiert werden.
Danach reicht ein einfaches `git clone https://github.com/LP16Goated4Real/TeamPlus-Zusage-Bot.git` im PowerShell Terminal.

---
### <ins>How To</ins>
#### **Konfiguration**
Öffne die Datei `config.yaml` mit Notepad oder einem ähnlichem Editor und gib deine TeamPlus-Logindaten ein (Speichern nicht vergessen!). Der Spitzname wird am Ende der Zusage-Nachricht automatisch hinzugefügt. 
 **Beispiel folgt:**
<img width="788" height="444" alt="config" src="https://github.com/user-attachments/assets/0bd7d3dd-c6eb-4800-8fdd-82a086241328" />

#### **Sprüche konfigurieren**
Um neue Sprüche hinzuzufügen, gehe in den **src**-Ordner und öffne die Datei `sprueche\.py`. Die neuen Sprüche müssen dasselbe Format wie die bereits existierenden haben.
#### **Windows Task Scheduler**
Damit das Skript wöchentlich ausgeführt wird, ist der Windows Task Scheduler nötig. 
1. Gehe dafür in die Windows Suchleiste und suche nach **Task Scheduler**.
2. Klicke danach auf **Action &rarr; create new task**.
3. Im Reiter *general*:
   - passenden Namen und Beschreibung eingeben
   - unter **Configure for** Windows 10 auswählen.
4. Reiter *Triggers* &rarr; **new...**.

<img width="576" height="442" alt="trigger" src="https://github.com/user-attachments/assets/be903818-de99-4f73-937d-a047d39c5f0d" />

5. Reiter *Actions* &rarr; **new...** &rarr; **Browse...** &rarr; wähle die Datei `auto_training_zusagen.bat` aus dem heruntergeladenen ZIP oder git repo aus
   - gehe sicher, dass die *Action* **Start a program** ist.
6. im Reiter *Settings*
   - **Run task as soon as possible after a scheduled start is missed** auswählen
   - **Stop the task if it runs longer than:** auf die kleinstmögliche Zeit stellen.
> [!IMPORTANT]
> Das Skript verarbeitet nur bereits in TeamPlus eingetragene Events, und nur Events, die in derselbe Woche stattfinden.
**Beispiel:** Läuft das Skript am Mittwoch, werden nur Events bis Sonntag Mitternacht berücksichtigt.

#### **Manuell starten**
Um das Skript unabhängig vom Zeitpunkt zu starten, rechtsclicke in der heruntergeladenen ZIP-Datei auf `auto_training_zusage.bat` und wähle **als Administrator ausführen**.

> [!NOTE]
> Jedes Mal, wenn das Skript läuft, werden alle Aktionen, Schritte und Fehler in der Datei `Log\bot.log` protokolliert.

<br>
<br>
©LP16Goated4RealAG
