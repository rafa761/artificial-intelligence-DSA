import math


def generate_primes(max_num):
    if isinstance(max_num, float):
        raise TypeError("Numero Float nao pode ser usado")
    if max_num is None:
        raise TypeError("None Nao pode ser usado")

    resultados = []
    for num in range(2, max_num + 1):
        for divisor in range(1, max_num + 1):
            if (num % divisor == 0) and (divisor not in (1, num)):
                resultados.append(False)
                break
        resultados.append(True)
    return resultados


if __name__ == "__main__":
    print(generate_primes(20))
# [False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True]