#EXERCÍCIO: implemente o exemplo de switch case acima usando as condições "if/else"
#Prompt: para cada dígito entre 0-9, o programa imprimirá uma confirmação 
#para o valor inserido ou irá imprimir "invalid inputs" para todos os outros números.

'''
number = input("Digite um número de 0-9: ")

if number == '0':
    print("Valor inserido [0]!")
elif number == '1':
    print("Valor inserido [1]!")
elif number == '2':
    print("Valor inserido [2]!")
elif number == '3':
    print("Valor inserido [3]!")
elif number == '4':
    print("Valor inserido [4]!")
elif number == '5':
    print("Valor inserido [5]!")
elif number == '6':
    print("Valor inserido [6]!")
elif number == '7':
    print("Valor inserido [7]!")
elif number == '8':
    print("Valor inserido [8]!")
elif number == '9':
    print("Valor inserido [9]!")
else:
    print("Número inválido!")
'''

def switcher(number):
 
  return {
    '0':"Valor inserido [0]!",
    '1':"Valor inserido [1]!",
    '2':"Valor inserido [2]!",
    '3':"Valor inserido [3]!",
    '4':"Valor inserido [4]!",
    '5':"Valor inserido [5]!",
    '6':"Valor inserido [6]!",
    '7':"Valor inserido [7]!",
    '8':"Valor inserido [8]!",
    '9':"Valor inserido [9]!",
  }.get(number,"Número inválido!")

number = input("Digite um número de 0-9: ")
print(switcher(number))
