import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    height = np.array(height)
    weight = np.array(weight)
    print(type(height))
    print(type(weight))
    bmi = weight / height**2
    return bmi.tolist()


# def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
#     return 

def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))

if __name__ == '__main__':
    main()