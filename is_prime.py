import math
from random import randint


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True


if __name__ == '__main__':

    MIN_VALUE = 0
    MAX_VALUE = 999
    random_number = randint(MIN_VALUE, MAX_VALUE)

    print(f'Is number \'{random_number}\' a prime? - {is_prime(random_number)}')
