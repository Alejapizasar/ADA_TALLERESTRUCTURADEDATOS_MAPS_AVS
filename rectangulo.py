#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    pila = []   # guarda INDICES de barras, con alturas crecientes
    mejor = 0
    n = len(h)

    # Recorre hasta n (una posicion extra) con altura 0 como "centinela"
    # para obligar a vaciar la pila al final
    for i in range(n + 1):
        if i < n:
            actual = h[i]
        else:
            actual = 0

        # Mientras la barra de la cima sea mas alta que la actual,
        # esa barra ya no puede seguir creciendo hacia la derecha
        while pila and h[pila[-1]] > actual:
            altura = h[pila.pop()]

            # Limite izquierdo: la nueva cima (primera barra menor a la izquierda)
            if pila:
                izquierda = pila[-1]
            else:
                izquierda = -1

            # Limite derecho: i (primera barra menor a la derecha)
            ancho = i - izquierda - 1
            mejor = max(mejor, altura * ancho)

        pila.append(i)

    return mejor

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
