'''
Validação de preço e código de origem do produto.
1 - Sul
2 - Norte
3 - Leste
4 - Oeste
5 ou 6 - Nordeste
7, 8 ou 9 - Sudeste
10 até 20 - Centro Oeste

'''
preco = 0.0
origem = 0

def switcher(origem):
    match origem:
        case 1:
            return "1 - Sul"
        case 2:
            return "2 - Norte"
        case 3:
            return "3 - Leste"
        case 4:
            return "4 - Oeste"
        case 5 | 6:
            return "5 ou 6 - Nordeste"
        case 7 | 8 | 9:
            return "7, 8 ou 9 - Sudeste"
        case _ if 10 <= origem <= 20:
            return "10 até 20 - Centro Oeste"
        case _:
            return "Produto importado!"

# Programa principal
try:
    preco = float(input("Digite o preço: "))
    origem = int(input("Digite o número da origem: "))
    print(switcher(origem))
except ValueError:
    print("Erro! Digite valores válidos.")