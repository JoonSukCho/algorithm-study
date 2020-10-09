
import sys

a, b = map(int, sys.stdin.readline().split())


def max_add(num1, num2):
    return num1 + num2


def max_sub(num1, num2):
    return max(num1 - num2, num2 - num1)


def max_mul(num1, num2):
    return num1 * num2


def max_div(num1, num2):
    return max(num1 / num2, num2 / num1)


def max_pow(num1, num2):
    return max(num1 ** num2, num2 ** num1)


print('%.6f' % max(max_add(a, b), max_sub(a, b), max_mul(
    a, b), max_div(a, b), max_pow(a, b)))
