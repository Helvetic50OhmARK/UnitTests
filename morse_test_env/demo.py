"""
Kleines Demo-Skript zum manuellen Ausprobieren in PyCharm.

Einfach mit Rechtsklick -> "Run 'demo'" ausführen, oder die Funktion
to_readable() in der Python-Konsole importieren und eigene Texte testen:

    from demo import to_readable
    from morse import Morse
    print(to_readable(Morse.convert_to_morse_code("sk")))
"""

from morse import Morse

SYMBOLS = {1: ".", 2: "-"}


def to_readable(result):
    """
    Wandelt die dit/dah-Liste in eine lesbare Darstellung um.
    Jeder Eintrag in `result` ist EIN Buchstabe bzw. EIN Prosign-Block.
    Zwischen solchen Blöcken steht ein Leerzeichen, innerhalb eines Blocks
    nicht - genau das macht den Unterschied zwischen "zwei Buchstaben mit
    Lücke" und "ein Prosign ohne Lücke" sichtbar.
    """
    parts = []
    for entry in result:
        if entry == [3]:  # Wortlücke
            parts.append("/")
        else:
            parts.append("".join(SYMBOLS[x] for x in entry))
    return " ".join(parts)


if __name__ == "__main__":
    samples = [
        "sk",            # Prosign -> EIN durchgehender Block: ...-.-
        "ar",            # Prosign
        "bk",            # Prosign
        "correction",    # Prosign
        "sos",           # normales Wort -> drei Blöcke (s, o, s)
        "cq sk de",      # Prosign eingebettet in einen Satz
        "war",           # enthält "ar" als Substring, ist aber kein Prosign
        "q",             # enthält "q" als einzelnes Zeichen, ist kein Prosign
    ]

    for text in samples:
        result = Morse.convert_to_morse_code(text)
        readable = to_readable(result)
        # Anzahl der Blöcke ohne die Wortlücken-Marker [3] mitzuzählen:
        n_blocks = sum(1 for entry in result if entry != [3])
        print(f"{text!r:15} -> {readable:20} ({n_blocks} Block(e))")
