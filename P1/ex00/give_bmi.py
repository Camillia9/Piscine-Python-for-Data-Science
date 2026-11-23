import numpy as np

# Numpy est une librairie permetant la manipulation de tableau


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    # 1. Convertir la list en numpy pour le calcul
    # 2. Faire le calcul
    # 3. Renvoyer le resultat en LIST
    if len(height) != len(weight):
        raise AssertionError("height and weight must have the same length")

    if not all(
        isinstance(x, (int, float)) and not isinstance(x, bool)
        for x in height + weight
    ):
        raise AssertionError("height and weight must contain int or float")

    if not all(x > 0 for x in height + weight):
        raise AssertionError("height and weight must be strictly positive")

    height_arr = np.array(height)
    weight_arr = np.array(weight)
    bmi = weight_arr / height_arr**2
    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    # 1. Convertit la list en numpy pour faire l'operation
    # 2. Return une list

    if not all(
        isinstance(x, (int, float)) and not isinstance(x, bool)
        for x in bmi + [limit]
    ):
        raise AssertionError("bmi and limit must contain int or float")

    if not all(x > 0 for x in bmi + [limit]):
        raise AssertionError("bmi and limit must be strictly positive")

    value = np.array(bmi)
    return (value > limit).tolist()
