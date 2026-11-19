import os


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    try:
        width = os.get_terminal_size().columns
    except OSError:
        width = 80
    # Save la place de gauche
    suffix_max = f"]| {total}/{total}"
    # widht contient toute la longueur du term mais il faut retirer
    # l'espace besoin a gauche et a droite
    bar_length = width - len("100%|[") - len(suffix_max) - 1
    for i, elem in enumerate(lst, start=1):
        percent = int(i / total * 100)
        filled = max(1, int(i / total * bar_length))
        # ljust() rajoute les espaces vide a droite jusqua la fin de la bar
        bar = ("=" * (filled - 1) + ">").ljust(bar_length)
        print(f"\r{percent:3d}%|[{bar}]| {i}/{total}", end="", flush=True)
        yield elem
