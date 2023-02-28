verificador=int(input("Digite um numero inteiro positivo para verificar se ele faz parte da sequencia fibonacci: "))

if(verificador<0):
    print("Não é possivel verificar este número")
else:
    fib = [0, 1] 
    for i in range(2, 20):
        fib.append(fib[i-1] + fib[i-2]) 

    print(fib)
    if verificador in fib:
        print (f'O número {verificador} pertence à sequencia de fibonacci')
    else:
        print (f'O número {verificador} não pertence à sequencia de fibonacci')