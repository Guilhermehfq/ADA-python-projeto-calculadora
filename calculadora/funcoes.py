def soma(a, b):
    if isinstance(a, int or float) and isinstance(b, int or float):
        soma = a + b
        return soma
    else:
        print(TypeError(f'O input {a} e {b} devem ser uma int ou float, recebido {a}, {type(a)}, {b} tipo {type(b)}'))

def subtracao(a, b):
    subtracao = a - b
    return subtracao

def divisao(a, b):
    if b != 0:
        subtracao = a / b
        return subtracao
    else:
        print(TypeError('Não é possivel dividir por 0'))

def multiplicação(a, b):
    if isinstance(a, int or float) and isinstance(b, int or float):
        multiplicação = a * b
        return multiplicação
    else:
        print(TypeError(f'O input {a} e {b} devem ser uma int ou float, recebido {a}, {type(a)}, {b} tipo {type(b)}'))