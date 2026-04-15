def calcular_media():

    valores = []
    
    try:
        for indice in range(3):
            numero = float(input(f"Digite o {indice+1}º valor: "))
            valores.append(numero)
        
        resultado = sum(valores) / 3
        print(f"Média final: {resultado:.2f}")
    
    except ValueError:
        print("Erro: as notas devem ser numéricas.")




def calcular_total():
    
    try:
        item1 = float(input("Digite o valor do primeiro item: "))
        item2 = float(input("Digite o valor do segundo item: "))
        
        soma = item1 + item2
        print(f"Valor total da compra: R$ {soma:.2f}")
    
    except ValueError:
        print("Erro: os preços devem ser numéricos.")