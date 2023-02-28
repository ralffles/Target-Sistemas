string = "Rafael Isaac"
lista = list(string)
for i in range(len(lista) // 2):
    temp = lista[i]
    lista[i] = lista[len(lista) - 1 - i]
    lista[len(lista) - 1 - i] = temp
string_invertida = ''.join(lista)
print(string_invertida)