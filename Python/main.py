__author__ = 'Bartłomiej Garbacz'
__copyright__ = 'Copyright: © 2021 etc... If u need it just send me an e-mail'
__version__ = 'Python-3.9'
__email__ = 'bartigarbacz@gmail.com / bartlomiej.garbacz@student.wat.edu.pl'
__username__ = 'b-garbacz'
__date__ = '13.02.2021'
__Description__ = 'Implementation of RSA cryptosystem'

from RSA import *
import random
import time


def emulator_rsa(n):
    """
    Simple emulator of RSA which one encrypt and decrypt random data
    :param n: security parameter
    :return: success or failure
    """
    plaintext = random.randint(10, 100)
    print("plaintext=", plaintext)
    priv, pub = RSA.generator(n)
    ciphertext = RSA.encrypt(plaintext, pub)
    print("encrypted=", ciphertext)
    decrypted_plaintext = RSA.decrypt(ciphertext, priv)
    print("decrypted=", decrypted_plaintext)
    if plaintext == decrypted_plaintext:
        return True
    return False


if __name__ == '__main__':
    print('Author: ' + __author__)
    print('Copyright: ' + __copyright__)
    print('Version: ' + __version__)
    print('Email: ' + __email__)
    print('Date: ' + __date__)
    print('Username: ' + __username__)
    print('Description: ' + __Description__)
    print("\n")

    print("--------------------128--------------------")
    start = time.time()
    emulator_rsa(128)
    print(time.time() - start)
    print("--------------------256--------------------")
    start = time.time()
    emulator_rsa(256)
    print(time.time() - start)
    print("--------------------512--------------------")
    start = time.time()
    emulator_rsa(512)
    print(time.time() - start)
    print("--------------------1024-------------------")
    start = time.time()
    emulator_rsa(1024)
    print(time.time() - start)
    print("--------------------2048-------------------")
    start = time.time()
    emulator_rsa(2048)
    print(time.time() - start)
    print("-------------------------------------------")
