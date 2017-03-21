import math
import Input
import Output
import bisect


def main():
    manual_input()
    print('Another one?')
    repeat = input('\'Y\' \'N\':')
    while repeat.lower() == 'y':
        manual_input()
        print('Another one?')
        repeat = input('\'Y\' \'N\':')


def manual_input():
    n = Input.insert_number()
    divisors = get_divisors(n)
    print('Divisors: ' + str(divisors))
    get_matrix(divisors, n)


def get_divisors(n):
    divisors = []
    limit = int(str(math.sqrt(n)).split('.')[0])
    for i in range(1, limit + 1):
        if n % i == 0:
            bisect.insort(divisors, i)
            if i != (n / i):
                bisect.insort(divisors, n / i)
    return divisors


def get_matrix(divisors, n):
    length = len(divisors)
    matrix = []
    for i in range(length - 1, -1, -1):
        arr = []
        for j in range(length - 1, -1, -1):
            if divides(divisors[j], divisors[i]):
                arr.append(1)
            else:
                arr.append(0)
        matrix.append(arr)
    Output.print_matrix(matrix)
    Output.save_diagram(divisors, matrix)


def divides(x, y):
    return y % x == 0


def print_number(n):
    print('{' + str(n) + '}')


def print_line():
    print('--------------------')


main()
