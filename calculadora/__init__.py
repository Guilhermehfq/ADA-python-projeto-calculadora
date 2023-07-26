from funcoes import soma
from funcoes import subtracao
from funcoes import divisao
from funcoes import multiplicação

def calcule():
    loop = True
    while loop == True:
        a = input('Escolha o numero [a]: ')
        b = input('Escolha o numero [b]: ')
        escolha = input("""
                        Escolha a operação que voce deseja realizar:
                        [soma] [+] -> Somar
                        [subtracao] [-] -> Subtrair
                        [divisao] [/] -> Dividir
                        [multiplicação] [*] -> Multiplicar
                        [fechar] -> Fechar o programa
                        """)
        if escolha == 'soma' or '+':
            resultado = soma(a, b)
            print(f'O resultado de {a} + {b} = {resultado}')
        elif escolha == 'subtracao' or '-':
            resultado = subtracao(a, b)
            print(f'O resultado de {a} - {b} = {resultado}')
        elif escolha == 'divisao' or '/':
            resultado = divisao(a, b)
            print(f'O resultado de {a} / {b} = {resultado}')
        elif escolha == 'multiplicação' or '*':
            resultado = multiplicação(a, b)
            print(f'O resultado de {a} * {b} = {resultado}')
        elif escolha == 'fechar':
            print('Fechando o programa...')
            loop = False
        else:
            print(f'O operador {escolha} é invalido, tente novamente')