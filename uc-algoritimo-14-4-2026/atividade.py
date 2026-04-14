def soma_segura(num1, num2):
    try:
        return num1 + num2
    except TypeError:
        print("Entrada inválida")
        return 0


def divisao(valor1, valor2):
    try:
        return valor1 / valor2
    except ZeroDivisionError:
        return "Não divida por zero!"