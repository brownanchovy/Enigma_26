# constant N is given and return list shuffled by random library
# list will rotate on rotate.py and use inverse function using index

from random import seed, shuffle

def rotor(n: int) -> list:
    seed(n)
    rotate = [i for i in range(1, 27)]
    shuffle(rotate)
    print(rotate)
    return rotate
