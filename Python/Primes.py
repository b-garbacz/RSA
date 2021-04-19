__author__ = 'Bartłomiej Garbacz'
__copyright__ = 'Copyright: © 2021 etc... If u need it just send me an e-mail'
__version__ = 'Python-3.9'
__email__ = 'bartigarbacz@gmail.com / bartlomiej.garbacz@student.wat.edu.pl'
__username__ = 'b-garbacz'
__date__ =  '13.02.2021'
__Description__ = 'Implementation of RSA cryptosystem and Wiener"s attack '

import random
from Arithmetic import fast_p


def miller_rabin_test(n, k) -> bool:
    """
    Not working.
    TODO -  fix the error for  infinite computation for large numbers
    :param n:
    :param k:
    :return:
    """

    if n <= 1:
        return False

    if n % 2 == 0:
        return False
    s = 0
    d = n - 1
    while d % 2 == 0:
        s, d = s + 1, int(d / 2)
    for _ in range(k):
        a = random.randint(1, n - 1)
        x = fast_p(a, d, n)
        if x != 1:
            for r in range(0, s):
                if x != n - 1:
                    x = fast_p(x, 2, n)
                else:
                    break
            else:
                return False
    return True


def fermat(n, k) -> bool:
    """
    Algorith is using Little Fermat's Little Theorem to check if a number is prime.
    :param n: a value to test for primality
    :param k:  a parameter that determines the number of times to test for primality
    :return: composite if n is composite, otherwise probably prime
    """
    if n % 2 == 0:
        return False
    for i in range(k):
        a = random.randint(2, n - 2)
        if fast_p(a, n - 1, n) != 1:
            return False
    return True


def random_prime(a, b):
    '''
    Simple generator  a random prime number using a given numerical interval
    :param a: first integer
    :param b: second integer
    :return: Prime number
    '''
    while True:
        random_integer = random.randint(a, b)
        if fermat(random_integer, 16) == True:
            return random_integer