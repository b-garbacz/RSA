__author__ = 'Bartłomiej Garbacz'
__copyright__ = 'Copyright: © 2021 etc... If u need it just send me an e-mail'
__version__ = 'Python-3.9'
__email__ = 'bartigarbacz@gmail.com / bartlomiej.garbacz@student.wat.edu.pl'
__username__ = 'b-garbacz'
__date__ = '13.02.2021'
__Description__ = 'Implementation of RSA cryptosystem'

from Primes import *
from Arithmetic import *


class RSA(object):
    def __init__(self):
        self._key_size = None
        self._e = None
        self.__d = None
        self._N = None
        self._public = (self._e, self._N)
        self.__private = (self.__d, self._N)

    @staticmethod
    def get_prime(key_size):
        """
        A Method which one draws prime numbers while their product is equal to the bit length of security parametr
        :param key_size: Bit lenght  of the security parameter from generator method
        :return: Two prime numbers whose product bit lenght is equal to the security parameter
        """
        half_key_size = math.floor(key_size / 2)
        while True:
            p = random_prime(2**(half_key_size - 1), 2**(half_key_size + 2))
            q = random_prime(2**(half_key_size - 1), 2**(half_key_size + 2))
            if len(bin(p * q)[2:]) == key_size:
                perfect_p = p
                perfect_q = q
                break
        return perfect_p, perfect_q

    @classmethod
    def generator(cls, key_size) -> object:
        """
        Generator of basic RSA parameters which one returns private key and public key.
        :param key_size: Bit lenght  of the security parameter
        :return: Pair of keys.
        """
        while True:
            if key_size < 8:
                print("lenght of N must be greater than or equal to 8")
                return False
            p, q = RSA.get_prime(key_size)
            N = p * q
            FE = (p - 1) * (q - 1)
            e = relativelyprime(FE)
            d = privateexponent(e, FE)
            if ((e * d) % FE == 1) and e != d:
                cls._public = (e, N)
                cls._private = (d, N)
                del q
                del p
                return cls._private, cls._public

    @classmethod
    def encrypt(cls, plaintext, public) -> object:
        """
        A method that performs the congruence c = p^{e} % N
        :param plaintext: Plaintext to encrypt
        :param public: Tuple that consisting of public exponent and Module
        :return: ciphertext
        """
        ciphertext = fast_p(plaintext, public[0], public[1])
        return ciphertext

    @classmethod
    def decrypt(cls, ciphertext, private) -> object:
        """
        A method that performs the congruence p = c^{d} % N
        :param ciphertext: ciphertext to decrypt
        :param private: Tuple that consisting of private exponent and Module
        :return: plaintext
        """
        plaintext = fast_p(ciphertext, private[0], private[1])
        return plaintext

    def __del__(self):
        print("cleared")
