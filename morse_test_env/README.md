# Morse-Prosign-Fix – Testumgebung

Dieses Paket enthält die korrigierte `morse.py` sowie eine Testsuite und ein
kleines Demo-Skript, mit denen sich der Prosign-Fix lokal in PyCharm
nachvollziehen lässt.

## Enthaltene Dateien

| Datei            | Zweck                                                          |
|-------------------|------------------------------------------------------------------|
| `morse.py`        | Korrigierte Quelldatei (Prosigns werden als ein Block erkannt)  |
| `test_morse.py`   | Pytest-Testsuite mit Fokus auf das Prosign-Verhalten             |
| `demo.py`         | Kleines Skript zum manuellen Ausprobieren / visuellen Vergleich  |
| `requirements.txt`| Benötigte Pakete (`mistletoe`, `pytest`)                         |

## Setup in PyCharm

1. **Projektordner öffnen**
   Diesen entpackten Ordner in PyCharm als Projekt öffnen
   (`File > Open...` und den Ordner auswählen).

2. **Interpreter / virtuelle Umgebung einrichten**
   `File > Settings > Project: <Name> > Python Interpreter`
   → Zahnrad-Symbol → `Add...` → `Virtualenv Environment` → `New environment`
   (Python 3.9 oder neuer empfohlen) → OK.

3. **Abhängigkeiten installieren**
   Terminal in PyCharm öffnen (unten im Fenster) und ausführen:
   ```bash
   pip install -r requirements.txt
   ```

4. **Pytest als Standard-Testrunner einstellen (falls nötig)**
   `File > Settings > Tools > Python Integrated Tools`
   → unter „Testing“ → „Default test runner“ → `pytest` auswählen.

5. **Tests ausführen**
   Rechtsklick auf `test_morse.py` im Projektbaum
   → `Run 'pytest in test_morse.py'`.
   Alle 13 Tests sollten grün sein.

   Alternativ im Terminal:
   ```bash
   pytest -v
   ```

6. **Manuell ausprobieren**
   Rechtsklick auf `demo.py` → `Run 'demo'`, oder die Python-Konsole nutzen:
   ```python
   from morse import Morse
   Morse.convert_to_morse_code("sk")
   ```
   Ein korrekt erkanntes Prosign liefert genau **einen** Listeneintrag
   (z. B. `[[1, 1, 1, 2, 1, 2]]` für „sk“) statt zwei getrennter Buchstaben
   mit Lücke dazwischen.

## Worauf die Tests besonders achten

- `ar`, `bk`, `sk`, `correction` werden jeweils als **ein** zusammenhängender
  dit/dah-Block zurückgegeben (das eigentliche Bugfix-Ziel).
- Groß-/Kleinschreibung bei Prosigns spielt keine Rolle (`"SK"` == `"sk"`).
- Ein Prosign mitten im Satz (`"cq sk de"`) bleibt weiterhin als ein Block
  erhalten.
- Normale Wörter, auch solche, die zufällig die Buchstabenfolge eines
  Prosigns als Teilstring enthalten (z. B. `"war"` enthält `"ar"`), werden
  unverändert buchstabenweise verarbeitet – das war vorher schon korrekt
  und darf durch den Fix nicht kaputtgehen.

## Hinweis

Die bekannte Einschränkung: Das Wort `"correction"` selbst kollidiert mit
dem gleichnamigen Prosign-Signal. Wird `[morse:correction]` eingegeben, wird
immer das Prosign-Signal erzeugt, nie die buchstabierte Version des Wortes.
Das ist eine bewusste Design-Entscheidung des bestehenden Dictionaries und
keine Nebenwirkung dieses Fixes.
