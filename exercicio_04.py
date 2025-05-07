def somar_pares(lista):
    total = 0
    for i in lista:
            total += i
    media = total /len(lista) 
    return media

numeros = [1, 2, 3, 4, 5, 6]

print(somar_pares(numeros))