'''
Melhoria a validação de cálculo da média aritmética 
entre as quatro notas e 
verifica se foi aprovado por média.
'''
n1 = n2 = n3 = n4 = media = 0.0 

try:
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    n4 = float(input("Digite a quarta nota: "))

    media = (n1 + n2 + n3 + n4) / 4
    
    if media >= 8:
        print("Aprovado! Sua média está superior a 7: ", media)
    else:
          print("Reprovado! Sua média está abaixo de 8: ", media)

except ValueError:
    print("Erro! Favor digitar um número válido.")