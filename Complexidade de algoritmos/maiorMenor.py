# implentar um programa que recebe uma lista e aponta o maior e o menor; avaliar a complexidade

lista = [8,7,7,4,2,2,0,3,-9,1,8]

def funcao():
    maior = menor = lista[0]
    
    for i in range(1, len(lista)):
        if menor > lista[i]:
            menor = lista[i]
            
        if maior < lista[i]: # elif
            maior = lista[i]  
            #  5 4 3 2 1 
            
    tupla = (menor, maior)
    return tupla  

# A complexidade para buscar o menor e o maior elemento é de n-1, sendo "n" o número de elementos da lista; vão ser feitas n-1 comparações com um certo elemento. Nesse caso, como tem que avaliar o maior e o menor, a complexidade é de 2(n-1) 
# podemos diminuir a complexidade desse algoritmo trocando o segundo "if" por "elif", assim, o algoritmo só faz uma verificação. Então, para fazer a análise de complexidade desse algoritmo, considera-se o caso médio, que é a média entre o melhor caso e o pior caso. O melhor caso é quando o elif nunca é executado, ou seja, quando a lista está em ordem decrescente, nesse caso. Assim, a complexidade no melhor caso é n-1. No pior caso, o elif sempre é executado, acontece comparações duas vezes, então a complexidade é 2n-2; a média de complexidade será (3n-3)/2


# para diminuir ainda mais a complexidade do algoritmo, podemos implementar a busca binária: primeiramente, determina-se dois elementos aleatórios como menor e como maior; depois, comparar os números dois a dois, dividir em maior e menor e comparar esses com o maior e o menor pré-definidos

# lista = [8,7,7,4,2,2,0,3,-9,1,8,8]
# menor = 7, maior = 8
# duplas 2 -> 11
# duplas[indices]: 2,3 ; 4,5; 6,7; 8,9; 10,11

def busca_binaria():
    # se lista for ímpar, eu torno ela par 
    if len(lista)%2 != 0:
        lista.append(lista[0])
    
    if lista[0] < lista[1]:
        menor = lista[0]
        maior = lista[1]
    
    else:
        menor = lista[1]
        maior = lista[0]
        
    i = 2  
    # duplas[valores]: 7,4; 2,2; 0,3; -9,1; 8,8
    # menor = -9, maior = 8
    while(i < len(lista)):
        if lista[i] > lista[i+1]:
            if lista[i] > maior: 
                 maior = lista[i]
            if lista[i+1] < menor:
                menor = lista[i+1]
        else:
            if lista[i+1] > maior:
                maior = lista[i+1]
            if lista[i] < menor:
                menor = lista[i]
        i+=2
    tupla = (menor, maior)
    print(tupla)

busca_binaria()