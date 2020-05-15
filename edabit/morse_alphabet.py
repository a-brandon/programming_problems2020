def morse(txt):
    d = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
         "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
         "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
         "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
         "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
         " ": "....."}
    d = {**d, **{v: k for k, v in d.items()}}
    if txt[0].isalpha():
        return ' '.join(d[c.upper()] for c in txt)
    return ''.join(d[c] for c in txt.split())