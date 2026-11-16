import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
    "0": "----- "
}


def main():
    try:
        len_args = len(sys.argv[1:])

        if len_args != 1:
            raise AssertionError("the arguments are bad")

        value = sys.argv[1].upper()
        try:
            for letter in value:
                NESTED_MORSE[letter]
        except KeyError:
            raise AssertionError("the arguments are bad")

        morse = " ".join(NESTED_MORSE[i].strip() for i in value)
        # strip() retire les espaces en debut/fin d'une chaine de caracteres.
        # (j'en ai besoin pour retirer l'epace de fin du dico).
        # Du coup tout le morse est colle. J;ajoute un espace avec le join(" ")
        # qui lui ajoute des separateurs AU MILIEU seulement.

        print(morse)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == '__main__':
    main()
