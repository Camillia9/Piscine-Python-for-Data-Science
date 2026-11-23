from give_bmi import give_bmi
from give_bmi import apply_limit


def main():
    height = [2.71, 1.15]
    weight = [165.3, 43]

    try:
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, '43'))
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == '__main__':
    main()
