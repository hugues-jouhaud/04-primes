from math import sqrt
import numpy as np

#### Fonction secondaire


def isprime(p):
    nbrChoisi = p
    diviseursPotentiels =  int(np.ceil(np.sqrt(nbrChoisi)))
    for i in range(2,diviseursPotentiels+1):
        if nbrChoisi % i == 0:
            return False
    return True
    pass

#### Fonction principale


def main():

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
