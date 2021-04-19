__author__ = 'Bartłomiej Garbacz'
__copyright__ = 'Copyright: © 2021 etc... If u need it just send me an e-mail'
__version__ = 'Python-3.9'
__email__ = 'bartigarbacz@gmail.com / bartlomiej.garbacz@student.wat.edu.pl'
__username__ = 'b-garbacz'
__date__ =  '13.02.2021'
__Description__ = 'Implementation of RSA cryptosystem '
import random
import math
def gcd(a, b):
    """
    Simple Euclidean algorithm to calculate the freatest common divisor of two natural numbers a and b
    source of code: https://en.wikipedia.org/wiki/Euclidean_algorithm
    :param a: first natural number
    :param b: second natural number
    :return: GCD(a,b)
    """

    while b != 0:
        c = a % b
        a = b
        b = c
    return a


def dec2bin(x):
    """
    Converter from decimal system to binary
    :param x: decimal number
    :return: binary number-
    """
    y = bin(x)[2:]
    tab = []
    for i in range(0, len(y)):
        tab.append(int(y[i]))
    return tab


def xgcd(x, N) -> object:
    '''
    Extended Euclidean algorithm gcd(x,N) = ux +Nv = d
    :param x: first natural number
    :param N: second natural number
    :return: d, u, v
    '''
    if x > N:
        return False, False, False
    X, Y, R, S = 1, 0, 0, 1
    while N != 0:
        C = x % N
        Q = math.floor(x / N)
        x, N = N, C
        Rp, Sp = R, S
        R = X - Q * R
        S = Y - Q * S
        X, Y = Rp, Sp
    d = x
    u = X
    v = Y
    return d, u, v

def relativelyprime(FE):  # draw a number from a range (1,f) and  gcd(1,f)==1
    '''
    Algorithm for determining relatively Prime numbers to compute the public exponent
    :param FE: phi(N) = (p-1)(q-1)
    :return: e
    '''
    while True:
        e = random.randint(1, FE)
        if gcd(e, FE) == 1 and e != FE and e != 1:
            return e


def privateexponent(e, FE):
    '''
    Algorithm for determining the private exponent using the properties of the extended Euclidean algorithm
    :param e: public exponent
    :param FE: phi(N) = (p-1)(q-1)
    :return: private exponent
    '''
    resoult_euclides = xgcd(e, FE)
    d = resoult_euclides[1]
    if d < 0:
        d = d % FE
    return d


def fast_p(a, b, n) -> object:
    """
    Exponentiation by squaring algorithm a^{b} % n = c
    :param a: natural value
    :param b: natural value
    :param n: natural value
    :return: c = a^{b} % n
    """
    e = dec2bin(b)
    c = 1
    for i in range(0, len(e)):
        c = (c ** 2) % n
        if e[i] == 1:
            c = (c * a) % n
    return c