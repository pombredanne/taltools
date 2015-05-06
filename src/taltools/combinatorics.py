import functools
import operator


def n_choose_k(n, k):
    result = 1
    for i in range(k):
        result *= n - i
        result //= i + 1
    return result


def n_next_to_k(n, k):
    return functools.reduce(operator.mul, range(n, k, -1))
