'''
Calcula as raízes de uma equação de 2º grau.
'''
import math

x1 = x2 = delta = a = b = c = 0.0

try:
    a, b, c = map(float, input("Informe os três valores dos coeficientes (a, b, c): ").split())

    delta = (b ** 2) - (4 * a * c)

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Raiz 1 =", x1, "Raiz 2 =", x2)

    else:
        print("Não existem raízes reais!")

except ValueError:
    print("Erro! Favor digitar três números válidos.")