def conta(a, b, op):
    if op == '1': return a + b
    if op == '2': return a - b
    if op == '3': return a * b
    if op == '4': return a / b if b != 0 else "Erro: Divisão por 0"

while True:
    print("\n[1]+ [2]- [3]* [4]/ [0]Sair")
    x = input("Opção: ")

    if x == '0': 
        print("Fui!")
        break

    if x in ['1', '2', '3', '4']:
        n1 = float(input("N1: "))
        n2 = float(input("N2: "))
        print("Res:", conta(n1, n2, x))
    else:
        print("Invalido!")