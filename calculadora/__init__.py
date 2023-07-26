from .funcoes import divisao, multiplicação, soma, subtracao


def calcule():
    loop = True
    while loop == True:
        a = input('Escolha o numero [a]: ')
        if str.isnumeric(a):
            a = float(a)
        b = input('Escolha o numero [b]: ')
        if str.isnumeric(b):
            b = float(b)
        
        escolha = input("""
Escolha a operação que voce deseja realizar:
[soma] [+]
[subtracao] [-]
[divisao] [/]
[multiplicação] [*]
[fechar] -> Fechar o programa
""")
        if escolha == 'soma' or escolha == '+':
            resultado = soma(a, b)
            print(f'O resultado de {a} + {b} = {resultado}')
        elif escolha == 'subtracao' or escolha == '-':
            resultado = subtracao(a, b)
            print(f'O resultado de {a} - {b} = {resultado}')
        elif escolha == 'divisao' or escolha == '/':
            resultado = divisao(a, b)
            print(f'O resultado de {a} / {b} = {resultado}')
        elif escolha == 'multiplicação' or escolha == '*':
            resultado = multiplicação(a, b)
            print(f'O resultado de {a} * {b} = {resultado}')
        elif escolha == 'fechar':
            print('Fechando o programa...')
            loop = False
        else:
            print(f'O operador {escolha} é invalido, tente novamente')