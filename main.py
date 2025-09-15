from math import sqrt
import numpy as np

#### Fonction secondaire


def isprime(p):

    Max = 100
    for k in range(2, Max+1):
      nbrChoisi = k
      diviseursPotentiels =  int(np.ceil(np.sqrt(nbrChoisi)))
      nbrPremier=True
      for i in range(2,diviseursPotentiels+1):
        if nbrChoisi % i == 0:
          nbrPremier=False
          break
      if nbrPremier:
        print(nbrChoisi)
    

    pass

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
