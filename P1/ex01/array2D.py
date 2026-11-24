import numpy as np

# for row in family	: Les sous-listes
# for x in row	: Les éléments d'une sous-liste
# for row in family for x in row : Tous les éléments de toutes les sous-listes


def slice_me(family: list, start: int, end: int) -> list:
    if not isinstance(family, list) or not all(
        isinstance(elem, list) for elem in family
    ):
        raise AssertionError("Family must be a list of lists")

    if not family or not family[0]:
        raise AssertionError("Empty list")

    if not all(len(x) == len(family[0]) for x in family):
        raise AssertionError("Different list size")

    if not all(
        isinstance(x, (int, float)) and not isinstance(x, bool)
        for row in family
        for x in row
    ):
        raise AssertionError("Family must contain int or float")

    if not all(x > 0 for row in family for x in row):
        raise AssertionError("family must be strictly positive")

    if not all(
        isinstance(x, int) and not isinstance(x, bool)
        for x in [start, end]
    ):
        raise AssertionError("Start and end must be int")

    arr_family = np.array(family)
    print(f"My shape is : {arr_family.shape}")
    new_slice = arr_family[start:end]
    print(f"My new shape is : {new_slice.shape}")

    return new_slice.tolist()


def main():
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]

    try:
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == '__main__':
    main()
