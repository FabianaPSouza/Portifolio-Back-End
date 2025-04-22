'''
Validação de lados do triângulo 
equilátero, isósceles ou escaleno.
'''
a = b = c = 0.0 

try:
    a = float(input("Digite o primeiro lado: "))
    b = float(input("Digite o segundo lado: "))
    c = float(input("Digite o terceiro lado: "))
    
    # Verifica se os lados formam um triângulo válido
    if (a < b + c) and (b < a + c) and (c < a + b):
        if (a == b) and (b == c):
            print("Triângulo equilátero!")
        elif (a == b) or (b == c) or (c == a):
            print("Triângulo isósceles!")
        else:
            print("Triângulo escaleno!")
    else:
        print("Estes valores não formam um triângulo!")     

except ValueError:
    print("Erro! Favor digitar um número válido.")