from math import sqrt, floor


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

######Big 0##########
# time: O(n)
# space: O(1)


############Srt solu###########


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, floor(sqrt(n))+1):
        if n % i == 0:
            return False

    return True
